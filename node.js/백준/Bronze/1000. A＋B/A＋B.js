var fs = require('fs');
var val = fs.readFileSync(0, 'utf-8').trim().split(' ');

var a = parseInt(val[0]);
var b = parseInt(val[1]);

console.log(a+b);