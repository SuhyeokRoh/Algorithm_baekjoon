import sys

n, m = map(int, sys.stdin.readline().split())
compare = [sys.stdin.readline().split()[0] for _ in range(n)]
problem = [sys.stdin.readline().split()[0] for _ in range(m)]

result = 0
for x in problem:
    if x in compare:
        result += 1
print(result)