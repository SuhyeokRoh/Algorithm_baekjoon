let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', li => {
    input.push(li.trim());
}).on('close', _ => {
    bucket(input);
    process.exit();
})

function bucket(lst) {
    let [a,b] = lst[0].split(" ").map(el => parseInt(el));
    let arr = Array(a+1).fill().map((arr, i) => {
        return i
    });
    for(let i=1; i<=b; i++){
        let [m, n] = lst[i].split(" ").map(el=>parseInt(el));
        let tmp = arr.slice(m, n+1).reverse();
        arr.splice(m, n-m+1, ...tmp);
    }
    console.log(...arr.slice(1));
}