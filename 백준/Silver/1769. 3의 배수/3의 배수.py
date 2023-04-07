n = list(input())
cnt = 0
rst = 'NO'
if len(n) == 1:
    tmp = int(n[0])
else:
    while len(n) > 1:
        tmp = 0
        for x in n:
            tmp += int(x)
        cnt += 1
        if tmp < 10:
            break
        else:
            n = list(str(tmp))

if tmp % 3 == 0:
    rst = 'YES'
print(cnt)
print(rst)