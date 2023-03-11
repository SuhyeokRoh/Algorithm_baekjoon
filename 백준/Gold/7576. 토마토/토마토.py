from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()

delta_move = [(1,0), (0,1), (-1,0), (0,-1)]
cnt = 0
for i in range(N):
    cnt += arr[i].count(0)
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j, 0))

while q:
    row, col, day = q.popleft()

    for x, y in delta_move:
        if 0 <= row + x < N and 0 <= col + y < M:
            if not arr[row+x][col+y]:
                q.append((row+x, col+y, day+1))
                arr[row+x][col+y] = 1
                cnt -= 1

if not cnt:
    print(day)
else:
    print(-1)