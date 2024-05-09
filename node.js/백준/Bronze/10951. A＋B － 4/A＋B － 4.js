let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;
let answer = '';

rl.on('line', li => {
    input = li.split(' ');
    answer += makeStr(Number(input[0]), Number(input[1]));
}).on('close', _ => {
    console.log(answer);
    process.exit();
})

function makeStr(a, b) {
    return a + b + '\n'
}