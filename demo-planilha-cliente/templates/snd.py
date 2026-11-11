import json, numpy as np, wave
SR=44100; D=46.6; out=np.zeros(int(SR*(D+1)))
def env(n,dec): return np.exp(-np.linspace(0,dec,n))
def tone(f0,f1,dur,dec,amp,h=()):
    n=int(SR*dur); ph=2*np.pi*np.cumsum(np.linspace(f0,f1,n))/SR
    return amp*(np.sin(ph)+sum(a*np.sin(k*ph) for k,a in h))*env(n,dec)
def mix(*ws):
    m=np.zeros(max(len(w) for w in ws))
    for w in ws: m[:len(w)]+=w
    return m
rng=np.random.default_rng(1)
n1=int(SR*.035); n2=int(SR*.02)
S={'pop':tone(520,1250,.11,7,.45),
 'tick':mix(tone(2600,2400,.035,9,.22),.12*rng.standard_normal(n1)*env(n1,14)),
 'key':mix(.18*rng.standard_normal(n2)*env(n2,10),tone(1800,1700,.02,10,.08)),
 'cnt':tone(1900,1900,.025,8,.07),
 'ding':mix(tone(1318,1318,.9,5,.28,((2,.35),(3,.12))),np.concatenate([np.zeros(int(SR*.09)),tone(1976,1976,.7,5,.18)])),
 'coin':np.concatenate([tone(988,988,.07,4,.3),tone(1318,1318,.35,6,.3,((2,.2),))]),
 'error':np.concatenate([tone(196,190,.16,2,.35,((3,.3),)),np.zeros(int(SR*.05)),tone(165,160,.22,3,.35,((3,.3),))])}
n=int(SR*.45); sm=np.convolve(rng.standard_normal(n),np.ones(40)/40,'same'); S['whoosh']=.9*sm*np.sin(np.linspace(0,np.pi,n))**2
for t,k in json.load(open('sfx.json')):
    w=S[k]; i=int(t*SR); out[i:i+len(w)]+=w[:len(out)-i]
t=np.arange(len(out))/SR; pad=np.zeros_like(out)
chords=[(261.6,329.6,392.0),(220,261.6,329.6),(174.6,220,261.6),(196,246.9,293.7)]*4
for i,c in enumerate(chords):
    a=int(i*4*SR); b=min(len(out),a+int(4.2*SR))
    if a>=len(out): break
    tt=t[a:b]-t[a]; e=np.minimum(1,tt/.6)*np.clip((4.2-tt)/.6,0,1)
    pad[a:b]+=sum(np.sin(2*np.pi*f*tt)+.3*np.sin(4*np.pi*f*tt) for f in c)*e*.018
out=(out+pad)*np.clip(np.minimum(t/1.0,(D+.6-t)/1.5),0,1)
out=out/np.max(np.abs(out))*.85
with wave.open('sfx.wav','w') as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes())
