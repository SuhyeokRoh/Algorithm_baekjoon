import sys

loop = int(sys.stdin.readline())
lst = [0] * loop
for num in range(loop):
    x,y = map(int,sys.stdin.readline().split())
    lst[num] = (y,x)

lst.sort()

for idx in range(1,len(lst)):
    if lst[idx-1][0] == lst[idx][0]:
        if lst[idx-1][-1] > lst[idx][-1]:
            lst[idx-1], lst[idx] = lst[idx], lst[idx-1]

for y,x in lst:
    print(x,y)