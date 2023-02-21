N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
queue, visited[0][0] = [(0, 0)], 1
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while queue:
    row, col = queue.pop(0)
    for x, y in delta:
        nx = row + x
        ny = col + y
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[row][col] + 1
                
print(visited[N-1][M-1])