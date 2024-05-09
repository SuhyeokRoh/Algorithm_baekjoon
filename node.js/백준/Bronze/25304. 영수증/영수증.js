let li = require('fs').readFileSync(0).toString().split('\n');
let total = 0;
for(let i=0; i<Number(li[1]); i++) {
    let [price, cnt] = li[i+2].split(' ').map(el=> parseInt(el));
    total += price * cnt;
}

console.log(Number(li[0]) == total? "Yes" : "No");