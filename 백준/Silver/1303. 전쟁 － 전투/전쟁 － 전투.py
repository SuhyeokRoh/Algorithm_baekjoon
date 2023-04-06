from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]
delta = [(1,0), (0,1), (-1,0), (0,-1)]
rst = [0, 0]
for i in range(M):
    for j in range(N):
        if arr[i][j] == 'W':
            cnt = 1
            arr[i][j] = '_'
            q = deque()
            q.append((i, j))
            while q:
                row, col = q.popleft()
                for x, y in delta:
                    if 0 <= row + x < M and 0 <= col + y < N and arr[row+x][col+y] == 'W':
                        cnt += 1
                        arr[row+x][col+y] = '_'
                        q.append((row+x, col+y))
            rst[0] += cnt ** 2
        elif arr[i][j] == 'B':
            cnt = 1
            arr[i][j] = '_'
            q = deque()
            q.append((i, j))
            while q:
                row, col = q.popleft()
                for x, y in delta:
                    if 0 <= row + x < M and 0 <= col + y < N and arr[row+x][col+y] == 'B':
                        cnt += 1
                        arr[row+x][col+y] = '_'
                        q.append((row+x, col+y))
            rst[1] += cnt ** 2
        else:
            continue
print(*rst)