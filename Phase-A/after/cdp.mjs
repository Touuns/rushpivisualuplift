import fs from 'node:fs/promises';
export const dir = new URL('./', import.meta.url);
export const sleep = ms => new Promise(r => setTimeout(r, ms));
export async function connect() {
  const targets = await (await fetch('http://127.0.0.1:9228/json')).json();
  const target = targets.find(t => t.type === 'page');
  const ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r, {once:true}));
  let id = 0; const pending = new Map(); const handlers = new Map();
  ws.addEventListener('message', async e => {
    const m = JSON.parse(e.data);
    if (m.id) { const p = pending.get(m.id); pending.delete(m.id); m.error ? p?.reject(m.error) : p?.resolve(m.result); }
    else for (const h of handlers.get(m.method) || []) await h(m.params);
  });
  const send = (method, params={}) => new Promise((resolve,reject) => { const n=++id; pending.set(n,{resolve,reject}); ws.send(JSON.stringify({id:n,method,params})); });
  const on = (method, fn) => handlers.set(method,[...(handlers.get(method)||[]),fn]);
  const evaluate = async expression => { const r=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true}); if(r.exceptionDetails) throw new Error(JSON.stringify(r.exceptionDetails)); return r.result?.value; };
  const shot = async name => { const r=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false}); await fs.writeFile(new URL(name+'.png',dir),Buffer.from(r.data,'base64')); console.log('Captured',name); };
  const click = async text => { const found = await evaluate(`(()=>{const b=[...document.querySelectorAll('button')].find(b=>b.innerText.trim()===${JSON.stringify(text)}); if(!b)return false;b.click();return true})()`); if(!found)throw new Error('Button not found: '+text); await sleep(450); };
  const selector = async css => { await evaluate(`document.querySelector(${JSON.stringify(css)}).click()`); await sleep(450); };
  await send('Page.enable');await send('Runtime.enable');
  return {send,on,evaluate,shot,click,selector,close:()=>ws.close()};
}
if(process.argv[2]==='inspect') {const c=await connect(); console.log(await c.evaluate('document.body.innerText')); c.close();}
