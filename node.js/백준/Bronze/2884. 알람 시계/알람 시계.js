let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;

rl.on('line', function(li) {
    input = li.split(' ');
    rl.close();
}).on('close', function() {
    let a = parseInt(input[0]);
    let b = parseInt(input[1]);
    time(a, b);
    process.exit();
})

function time(a, b) {
    b = b - 45;
    if (b < 0) {
        a = a - 1;
        b = 60 + b;
    }
    a = (a < 0)? 24 + a : a;
    console.log(a, b);
}