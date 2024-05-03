let fs = require('fs');
let input = fs.readFileSync(0, 'utf-8').trim().split(' ');

let a = parseInt(input[0]);
let b = parseInt(input[1]);
const div = parseInt(a/b);

console.log(a+b);
console.log(a-b);
console.log(a*b);
console.log(div);
console.log(a%b);