let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input;

rl.on('line', function(li) {
    input = li.split(" ").map(el => parseInt(el));
    rl.close();
}).on('close', function() {
    const rst = (!(input % 4) && (input % 100))? 1 : (!(input % 400)? 1 : 0); 
    endProcess(rst);
    process.exit();
})

function endProcess(tmp) {
    console.log(tmp);
}