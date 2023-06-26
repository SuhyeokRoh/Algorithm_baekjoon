rst = 9*1+7*3+8*1+0*3+9*1+2*3+1*1+4*3+1*1+8*3

for i in range(3):
    num = int(input())
    if i % 2 == 0:
        rst += num
    else:
        rst += num * 3
print(f"The 1-3-sum is {rst}")