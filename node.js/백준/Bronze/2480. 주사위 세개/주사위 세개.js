let rl = require('readline').createInterface({
    input: process.stdin,
});

let input;

rl.on('line', function(li) {
    input = li.toString().split(' ').map(el => parseInt(el));
    rl.close();
}).on('close', function() {
    dice(input);
    process.exit();
});

function dice(lst) {
    let arr = Array.from({length: 7}, ()=>0);
    for(let i of lst) {
        arr[i] += 1;
    }
    
    if (arr.includes(3)) {
        console.log(10000 + 1000 * arr.indexOf(3));
    } else if (arr.includes(2)) {
        console.log(1000 + 100 * arr.indexOf(2));
    } else {
        console.log(arr.lastIndexOf(1) * 100);
    }
}