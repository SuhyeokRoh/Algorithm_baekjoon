let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;

rl.on('line', function(li) {
    input = li.split(' ').map(el => parseInt(el));
    rl.close();
}).on('close', function() {
    multiTable(input);
    process.exit();
});

function multiTable(a) {
    for(let i=1; i<10; i++) {
        let tmp = a * i;
        console.log(a + " * " + i + " = " + tmp);
    }
}