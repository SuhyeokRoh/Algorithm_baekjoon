let a = require('fs').readFileSync(0).toString();
let word = '';
for(let i=0; i<parseInt(Number(a)/4); i++) {
    word = word + 'long ';
}
console.log(word + 'int');