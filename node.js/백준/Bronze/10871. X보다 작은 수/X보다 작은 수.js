let li = require('fs').readFileSync(0).toString().split("\n");
let [a, b] = li[0].split(" ").map(el => parseInt(el));
let lst = li[1].split(" ").map(el => parseInt(el));
let rst = [];
lst.forEach(el => {
    if(el < b) {
        rst.push(el);
    }
});
console.log(...rst);