import sys

n = int(sys.stdin.readline())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    if distance == 0 and r1 == r2:
        print(-1)
    elif abs(r2 - r1) == distance or distance == r1 + r2:
        print(1)
    elif abs(r2 - r1) < distance < r1 + r2:
        print(2)
    else:
        print(0)