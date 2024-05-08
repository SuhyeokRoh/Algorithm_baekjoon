let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;

rl.on('line', function(li) {
    input = li.toString();
    rl.close();
}).on('close', function() {
    let a = Number(input)
    sumAll(a);
    process.exit();
})

function sumAll(a) {
    let tmp = parseInt(((a+1) * a) / 2);
    console.log(tmp);
}