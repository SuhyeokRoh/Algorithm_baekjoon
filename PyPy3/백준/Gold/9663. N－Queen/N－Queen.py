import sys


def queen(i):
    global n, rst

    if i == n:
        rst += 1
        return

    for x in range(n):
        if not used[x] and not usedUp[i+x] and not usedDown[i-x]:
            used[x] = usedUp[i+x] = usedDown[i-x] = True
            queen(i+1)
            used[x] = usedUp[i+x] = usedDown[i-x] = False


rst = 0
n = int(sys.stdin.readline().rstrip())
lst = [[0] * n for _ in range(n)]
used, usedUp, usedDown = [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)
queen(0)
print(rst)