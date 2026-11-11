const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:540,height:675},deviceScaleFactor:2});
await p.goto('file://'+__dirname+'/abas.html');await p.evaluate(()=>document.fonts.ready);
const names=['1_Como_usar','2_Produtos','3_Movimentacoes','4_Estoque_atual','5_Painel','6_Celular'];
for(let i=1;i<=6;i++) await p.locator('#s'+i).screenshot({path:`Aba_${names[i-1]}.png`});
await b.close();})();
