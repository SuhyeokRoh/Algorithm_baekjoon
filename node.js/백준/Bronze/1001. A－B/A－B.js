let readline = require('readline').createInterface({
   input: process.stdin,
   output: process.stdout,
});

let input = [];

readline.on('line', function(li) {
    input = li.split(' ').map(el => parseInt(el));
}).on('close', function() {
    const a = input[0];
    const b = input[1];
    console.log(a-b);
    process.exit();
});