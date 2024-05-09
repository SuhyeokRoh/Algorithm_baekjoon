let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;
let answer = '';
let i = 1;

rl.on('line', li => {
    input = li.split(' ');
    if (input.length == 2) {
        answer += makeStr(input[0], input[1], i);
        i++;
    }
}).on('close', _ => {
    console.log(answer);
    process.exit();
})

function makeStr(a, b, i) {
    return "Case #" + i + ": " + a + " + " + b + " = " + (Number(a)+Number(b)) + '\n';
}