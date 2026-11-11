const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:540,height:960},deviceScaleFactor:1});
await p.goto('file://'+__dirname+'/video.html');await p.evaluate(()=>document.fonts.ready);
for(const t of process.argv.slice(2)){await p.evaluate(t=>render(t),+t);await p.screenshot({path:`prev_${t}.png`});}
await b.close();})();
