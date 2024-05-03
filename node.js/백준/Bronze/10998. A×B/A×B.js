let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;

rl.on('line', function(el) {
    input = el.split(' ').map(el => parseInt(el));
    rl.close();
}).on('close', function() {
    console.log(input[0] * input[1]);
    process.exit();
});