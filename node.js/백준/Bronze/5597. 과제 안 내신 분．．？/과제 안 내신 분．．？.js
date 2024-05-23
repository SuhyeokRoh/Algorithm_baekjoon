let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

rl.on('line', li => {
    input.push(Number(li));
}).on('close', _ => {
    hw(input);
    process.exit();
});

function hw(lst) {
    let arr = Array(31).fill(0)
    lst.forEach(el => {
        arr[el]++;
    });
    arr.forEach((el, i) => {
        if(el == 0 && i) {
            console.log(i);
        }
    })
}