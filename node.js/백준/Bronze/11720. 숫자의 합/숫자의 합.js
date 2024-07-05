let rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', li => {
    input.push(li.trim());
}).on('close', _ => {
    sum(input);
    process.exit();
})

function sum(lst) {
    const n = Number(lst[0]);
    const nums = lst[1].split("").map(Number);
    let rst = 0, i = 0;
    while(i < n) {
        if(i+1 == n) {
            rst += Number(nums.slice(i).join(""));
            break;
        } else {
            rst += Number(nums[i]);
        }
        i++;
    }
    console.log(rst);
}