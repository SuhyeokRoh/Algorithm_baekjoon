let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

rl.on('line', li => {
    input.push(li.trim());
}).on('close', _ => {
    const lst = input[1].split(" ").map(el => parseInt(el));
    minMax(lst);
    process.exit();
});

function minMax(lst) {
    let min = 987654321, max = -987654321;
    lst.forEach(el => {
        if(el < min) {
            min = el;
        }
        
        if(el > max) {
            max = el;
        }
    });
    console.log(min, max);
}