let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

rl.on('line', li => {
    input.push(li.trim());
}).on('close', _ => {
    let [n,m] = input[0].split(" ").map(e => parseInt(e));
    ballChange(n, input.slice(1));
    process.exit();
});

function ballChange(n ,lst) {
    let rst = Array(n+1).fill().map((arr, i) => {
        return i
    });
    
    lst.forEach(el => {
        let [i, j] = el.split(" ").map(e => parseInt(e));
        [rst[i], rst[j]] = [rst[j], rst[i]];
    })
    
    console.log(...rst.slice(1));
}