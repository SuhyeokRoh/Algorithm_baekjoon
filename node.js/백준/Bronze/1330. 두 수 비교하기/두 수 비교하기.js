let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;

rl.on('line', function(li) {
    input = li.split(' ').map(el => parseInt(el));
    rl.close();
}).on('close', function() {
    const a = input[0];
    const b = input[1];
    result(a, b);
    process.exit();
})

function result(a, b) {
    console.log(a > b? ">" : (a < b? "<" : "=="));
}