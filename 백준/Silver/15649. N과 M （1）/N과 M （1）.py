import sys

m, n = map(int, sys.stdin.readline().split())
result = []

def recur(x, rst, visit):
    global result

    if x == n:
        result += [rst]
        return

    for i in range(1, m+1):
        if visit[i]:
            continue
        else:
            visit[i] = 1
            recur(x+1, rst + [i], visit)
            visit[i] = 0
    return

lst = [0 for k in range(m+1)]
for j in range(1, m+1):
    lst[j] = 1
    recur(1, [j], lst)
    lst[j] = 0

for l in result:
    print(*l, sep=" ")