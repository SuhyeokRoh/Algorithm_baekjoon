let rl = require('readline').createInterface({
    input: process.stdin,
})

let input = [];

rl.on('line', li => {
    input.push(li.trim());
}).on('close', _ => {
    FandL(input);
    process.exit();
})

function FandL(lst) {
    lst.slice(1,).forEach(i => {
        console.log(i[0]+i[i.length-1]);
    })
}