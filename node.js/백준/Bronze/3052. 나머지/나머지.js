let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', li=>{
    input.push(Number(li.trim()));
}).on('close', _ => {
    remainder(input);
    process.exit();
});

function remainder(lst) {
    let arr = Array(42).fill(0);
    
    lst.forEach(el => {
        arr[el%42]++;
    })
    
    const rst = arr.reduce((acc, cur) => {
        if(cur > 0) {
            return acc + 1; 
        } else {
            return acc
        }
    }, 0)
    
    console.log(rst)
}