from collections import deque

N = int(input())
visited = [[False] * N for _ in range(N)]
arr = [list(map(int, input())) for _ in range(N)]
rst, idx = [0], 0

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            idx += 1
            rst.append(1)
            visited[i][j] = True
            d = deque()
            d.append((i, j))
            while d:
                row, col = d.popleft()
                for x, y in delta:
                    if 0 <= row + x < N and 0 <= col + y < N:
                        if arr[row+x][col+y] and not visited[row+x][col+y]:
                            visited[row + x][col + y] = True
                            rst[idx] += 1
                            d.append((row+x, col+y))
print(idx)
rst.sort()
for i in range(1, idx+1):
    print(rst[i])