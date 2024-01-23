tf = [True] * 1000000
m = int(1000000 ** 0.5)
for i in range(2, m+1):
    if tf[i]:
        for j in range(i+i, 1000000, i):
            tf[j] = False
lst = set([i for i in range(2, 1000000) if tf[i]])

n = int(input())
for _ in range(n):
    x = int(input())
    rst = 0
    for i in lst:
        if i > x:
            continue
        if x - i >= i and x - i in lst:
            rst += 1
    print(rst)