rst = 987654321
for _ in range(int(input())):
    a,b = map(int, input().split())
    if a <= b:
        rst = min(rst, b)
print(rst)