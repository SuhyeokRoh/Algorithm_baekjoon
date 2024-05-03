let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];
let list = [];

rl.on('line', function(line) {
    input.push(line);
    
}).on('close', function() {
    input.forEach(el => {
        list.push(el.trim().split(' ').map(li => parseInt(el)));
    });
    let a = list[0];
    let b = list[1];
    let c = a * b;
    while(b > 0) {
        console.log(a * (b % 10));
        b = parseInt(b/10);
    }
    console.log(c);
    process.exit();
});