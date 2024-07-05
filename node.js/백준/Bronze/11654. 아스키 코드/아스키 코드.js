let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input;

rl.on('line', li => {
    input = li.trim();
    rl.close();
}).on('close', _ => {
    CharToAscii(input);
    process.exit();
})

function CharToAscii(word) {
    console.log(word.charCodeAt(0));
}