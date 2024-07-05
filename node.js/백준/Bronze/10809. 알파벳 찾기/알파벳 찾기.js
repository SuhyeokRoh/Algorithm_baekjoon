let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input;

rl.on('line', li => {
    input = li.trim();
    rl.close();
}).on('close', _ => {
    labeling(input);
    process.exit();
})

function labeling(word) {
    let alpabet = Array(26).fill(-1);
    word.split("").forEach((e,i) => {
        let n = e.charCodeAt(0) - 97;
        if(alpabet[n] === -1) {
            alpabet[n] = i;
        }
    })
    console.log(...alpabet);
}