N, r, c = map(int, input().split())
lst = []
idx = []
for i in range(N-1, -1, -1):
    lst.append(4**i)
    idx.append(2**i)
rst = 0

x = 0
while r != 0:
    if r - idx[x] >= 0:
        rst += lst[x] * 2
        r -= idx[x]
    else:
        x += 1
y = 0
while c != 0:
    if c - idx[y] >= 0:
        rst += lst[y]
        c -= idx[y]
    else:
        y += 1
print(rst)