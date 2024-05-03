let rl = require('readline').createInterface({
    input: process.stdin,
});

let input;

rl.on('line', function(el) {
    input = el.trim().split(' ').map(li => parseInt(li));
    rl.close();
}).on('close', function() {
    console.log(input - 543);
    process.exit();
});