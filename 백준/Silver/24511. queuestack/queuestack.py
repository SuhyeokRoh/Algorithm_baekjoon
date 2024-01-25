from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
st = list(map(int, sys.stdin.readline().split()))
i = 0
number = deque([])

for x in list(map(int, sys.stdin.readline().split())):
    if st[i] == 0:
        number.append(x)
    i += 1

m = int(sys.stdin.readline().rstrip())

for y in list(map(int, sys.stdin.readline().split())):
    number.appendleft(y)
    print(number.pop(), end=" ")
