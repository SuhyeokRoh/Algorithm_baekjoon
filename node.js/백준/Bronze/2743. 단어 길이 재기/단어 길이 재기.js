let rl = require('readline').createInterface({
    input: process.stdin,
})

let input;

rl.on('line', li => {
    input = li.trim();
}).on('close', _ => {
    cnt(input);
    process.exit();
})

function cnt(word) {
    console.log(word.length);
}