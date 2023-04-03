dic = {0:0, 1:3, 2:2, 3:1}
delta = [(-1,0), (0, -1), (1, 0), (0, 1)]

N, M = map(int, input().split())
x, y, d = map(int, input().split())
drc = dic[d]
arr = [list(map(int, input().split())) for _ in range(N)]


cnt = 0
while True:
    if not arr[x][y]:
        cnt += 1
        arr[x][y] = 2

    for r, c in delta:
        if 0 <= x+r < N and 0 <= y+c < M and not arr[x+r][y+c]:
            drc = (drc + 1) % 4
            if not arr[x+delta[drc][0]][y+delta[drc][1]]:
                cnt += 1
                arr[x + delta[drc][0]][y + delta[drc][1]] = 2
                x, y = x + delta[drc][0], y + delta[drc][1]
            break
    else:
        if arr[x - delta[drc][0]][y - delta[drc][1]] != 1:
            x, y = x - delta[drc][0], y - delta[drc][1]
        else:
            break
print(cnt)