let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;

rl.on('line', function(li) {
    input = li.trim();
    rl.close();
}).on('close', function() {
    const a = parseInt(input);
    resultPrint(input);
    process.exit();
})

function resultPrint(x) {
    if (x <= 100 && x >= 90) {
        console.log("A");
    } else if (x >= 80) {
        console.log("B");               
    } else if (x >= 70) {
        console.log("C");
    } else if (x >= 60) {
        console.log("D");
    } else {
        console.log("F");
    }
}