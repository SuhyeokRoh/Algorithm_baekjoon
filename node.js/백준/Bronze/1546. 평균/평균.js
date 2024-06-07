let rl = require('readline').createInterface({
    input: process.stdin,
})

let input = [];

rl.on('line', li => {
    input.push(li.trim());
}).on('close', _ => {
    avg(input);
    process.exit();
})

function avg(lst) {
    const cnt = Number(lst[0]);
    let arr = lst[1].split(" ").map(Number);
    const maxV = Math.max(...arr);
    const new_arr = arr.map(e => (e / maxV) * 100);
    let rst = new_arr.reduce((acc, cur) => acc + cur, 0);
    console.log(rst / cnt);
}