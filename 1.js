let request = function(id){
  return new Promise((resolve,reject)=>{
      //随机一个执行时间
      let time = Math.floor(10000*Math.random());
      console.log(`id为${id}开始请求,预计执行时间${time/1000}`)
      setTimeout(()=>{
          resolve(id);
      },time)
  }).then((id)=>{
      console.log(`id为${id}的请求进行逻辑处理`)
      return id;
  })
}
const pool = new Set()
let idArray = [0,1,2,3,4,5,6,7,8,9,10];
async function run(){
  for (let i=0;i<idArray.length;i++){
      let promise = request(idArray[i]);
      promise.then((res)=>{
          console.log(`id${res}的请求已经处理完毕,当前并发为${pool.size}`);
          pool.delete(promise)
          console.log(`当前并发为${pool.size}`);
      })
      pool.add(promise);
      //这里是重点，当满了就阻塞
      if (pool.size === 3){
          await Promise.race(pool);
      }
  }
}
run();
