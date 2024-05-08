let input = require('fs').readFileSync(0).toString().split('\n');

for(let i=1; i<=Number(input[0]); i++) {
    let [a, b] = input[i].split(' ').map(el => parseInt(el));
    plus(a, b);
}

function plus(a, b) {
    console.log(a+b);
}