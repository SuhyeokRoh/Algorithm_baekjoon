let fs = require('fs').readFileSync(0).toString().split('\n');
let [_, lst, a] = fs;
const cnt = lst.split(" ").filter(el => el == a).length;
console.log(cnt);