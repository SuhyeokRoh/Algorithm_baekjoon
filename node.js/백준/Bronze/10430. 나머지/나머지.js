let rl = require('readline').createInterface({
    input: process.stdin,
});

let input;

rl.on('line', function(line) {
    input = line.trim().split(' ').map(li => parseInt(li));
    rl.close();
}).on('close', function() {
    const [a, b, c] = input;
    console.log((a+b)%c);
    console.log(((a%c)+(b%c))%c);
    console.log((a*b)%c);
    console.log(((a%c)*(b%c))%c);
    process.exit();
})