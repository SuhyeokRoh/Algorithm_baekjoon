let readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;

readline.on('line', function(el) {
    input = el.split(' ').map(li => parseInt(li));
    readline.close();
}).on('close', function() {
    console.log(input[0] / input[1]);
    process.exit();
});