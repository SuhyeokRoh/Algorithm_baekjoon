let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', li => {
    input.push(li.trim());
}).on('close', _ => {
    sentence(input);
    process.exit();
})

function sentence(lst) {
    const word = lst[0];
    let nm = Number(lst[1]);
    console.log(word[nm-1]);
}