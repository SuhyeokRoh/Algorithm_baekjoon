let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [0];

rl.on('line', li => {
    input.push(Number(li.split(" ")));
}).on('close', _ => {
    maxV(input);
    process.exit();
});

function maxV(lst) {
    let max = 0, idx;
    lst.forEach((el, i) => {
        if(el > max) {
            max = el;
            idx = i;
        }
    });
    console.log(max);
    console.log(idx);
}