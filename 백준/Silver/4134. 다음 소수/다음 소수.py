import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0 or num == 1:
        print(2)
        continue
    while True:
        statement = 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                statement = 0
                break
        if statement == 1:
            rst = num
            break
        else:
            num += 1
    print(rst)