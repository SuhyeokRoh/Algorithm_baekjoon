let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', li => {
    input.push(li.trim())
}).on('close', _ => {
    let [n,m] = input[0].split(" ").map(el => parseInt(el));
    ball(n, input.slice(1));
    process.exit();
});

function ball(n, lst) {
    let rst = new Array(n+1).fill(0);
    lst.forEach(el => {
       let [i, j, k] = el.split(" ").map(e => parseInt(e));
       for(let m=i; m<=j; m++) {
           rst[m] = k;
       }
    });
    console.log(...rst.slice(1));
}