let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;

rl.on('line', li => {
    input = li.split(' ');
    rl.close();
}).on('close', _ => {
    for(let i=1; i<=Number(input); i++) {
        makeStar(Number(input), i);
    }
    process.exit();
})

function makeStar(a, i) {
    let word = '';
    for(let x=0; x<a-i; x++) {
        word += ' ';
    }
    for(let y=0; y<i; y++) {
        word += '*';
    }
    console.log(word);
}