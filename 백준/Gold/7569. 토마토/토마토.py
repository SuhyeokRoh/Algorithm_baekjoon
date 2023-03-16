from collections import deque

M, N, H = map(int, input().split())
lst = [[] for _ in range(H)]
q = deque()
cnt = 0
for i in range(H):
    lst[i] = [list(map(int, input().split())) for _ in range(N)]

    for j in range(N):
        cnt += lst[i][j].count(0)
        for k in range(M):
            if lst[i][j][k] == 1:
                q.append((i, j, k, 0))

delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1)]

while q:
    height, row, col, day = q.popleft()
    for z, y, x in delta:
        if 0 <= height + z < H and 0 <= row + y < N and 0 <= col + x < M:
            if not lst[height+z][row+y][col+x]:
                lst[height+z][row+y][col+x] = 1
                q.append((height+z, row+y, col+x, day+1))
                cnt -= 1
if cnt:
    print(-1)
else:
    print(day)