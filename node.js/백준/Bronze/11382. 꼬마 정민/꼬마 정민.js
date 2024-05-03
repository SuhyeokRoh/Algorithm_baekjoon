var input = require('fs').readFileSync('/dev/stdin').toString().split(' ');

var sum = input.reduce((partialSum, a) => partialSum + parseInt(a), 0);
solution(sum);

function solution(answer) {
    console.log(answer);
};