num = int(input())
num_list = list(range(1,num+1,1))
cnt = 0
for n in num_list:
    if n < 100:
        cnt += 1
    else:
        a = n // 100
        b,c = (n - a*100) // 10, (n - a*100) % 10
        if (a - b) == (b - c):
            cnt += 1
print(cnt)
