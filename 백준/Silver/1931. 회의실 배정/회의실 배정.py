import sys

input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    a = list(map(int, input().split()))
    lst.append(a)
lst.sort(key=lambda x: x[0])
lst.sort(key=lambda x: x[1])

rst, start = 1, lst[0][1]
for i in range(1, N):
    if lst[i][0] >= start:
        rst += 1
        start = lst[i][1]

print(rst)