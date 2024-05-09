let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;

rl.on('line', li => {
    input = li.split(' ');
    rl.close();
}).on('close', _ => {
    for(let i=1; i<= input; i++) {
        makeStar(i);
    }
    process.exit();
})

function makeStar(i) {
    let word = '';
    for(let x=0; x<i; x++) {
        word += '*';
    }
    console.log(word);
}