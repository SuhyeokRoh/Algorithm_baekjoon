let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;
let answer = '';

rl.on('line', li => {
    input = li.split(' ');
    
    if (input.length == 2) {
        let [a,b] = input.map(el => parseInt(el));
        answer += (a+b) + '\n';
    }
}).on('close', _ => {
    console.log(answer);
    process.exit();
})