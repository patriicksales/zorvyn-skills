const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:540,height:960},deviceScaleFactor:2});
await p.goto('file://'+__dirname+'/video.html');await p.evaluate(()=>document.fonts.ready);
fs.writeFileSync('sfx.json',JSON.stringify(await p.evaluate(()=>sfx())));
fs.mkdirSync('frames',{recursive:true});const N=Math.round(46.6*30);
for(let i=0;i<N;i++){await p.evaluate(t=>render(t),i/30);await p.screenshot({path:`frames/f${String(i).padStart(5,'0')}.jpg`,type:'jpeg',quality:92});}
await b.close();})();
