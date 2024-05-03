var rl = require('readline').createInterface({
    input: process.stdin,
});

let input;

rl.on('line', function(li) {
   input = li.trim();
   rl.close();
}).on('close', function() {
    console.log(input + '??!');
    process.exit();
});