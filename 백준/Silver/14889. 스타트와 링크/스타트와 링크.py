import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
lst = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
se_set = set(list(x for x in range(n)))
sequence = list(combinations([x for x in range(n)], n//2))
minV = 987654321

for x in sequence:
    tmp = se_set - set(x)
    if minV == 0:
        break
    a, b = 0, 0
    for i in x:
        for j in x:
            a += lst[i][j]
    for i in tmp:
        for j in tmp:
            b += lst[i][j]
    minV = min(minV, abs(a - b))
print(minV)
