N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
max_cnt = 1

for lst in arr:
    val = max(lst)
    if maxV < val:
        maxV = val

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for idx in range(1, maxV):
    lst = [[0 if x <= idx else x for x in li] for li in arr]
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] or not lst[i][j]:
                continue
            if lst[i][j] and not visited[i][j]:
                queue = [(i, j)]
                visited[i][j] = True
                while queue:
                    row, col = queue.pop(0)
                    for x, y in delta:
                        nx, ny = row + x, col + y
                        if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] and not visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)