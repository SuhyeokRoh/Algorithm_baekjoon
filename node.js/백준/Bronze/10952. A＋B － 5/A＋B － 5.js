let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;
let answer = '';

rl.on('line', li => {
    input = li.split(' ');
    if(input[0] == "0" && input[1] == "0") {
        rl.close();
    } else {
        answer += sumTotal(Number(input[0]), Number(input[1]));
    }
   
}).on('close', _ => {
    console.log(answer);
    process.exit();
})

function sumTotal(a, b) {
    return a + b + '\n';
}