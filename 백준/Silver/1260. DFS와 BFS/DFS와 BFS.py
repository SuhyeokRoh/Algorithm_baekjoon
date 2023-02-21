N, M, V = map(int, input().split())
arr_dfs = [[0] * (N+1) for _ in range(N+1)]
arr_bfs = [[] for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
rst_bfs, rst_dfs = [], []
stack, queue = [], [V]

for _ in range(M):
    x, y = map(int, input().split())
    arr_dfs[x][y] = 1
    arr_dfs[y][x] = 1
    arr_bfs[x].append(y)
    arr_bfs[y].append(x)

for i in range(1, N+1):
    arr_bfs[i] = sorted(arr_bfs[i])

visited_dfs[V] = True
rst_dfs.append(V)

while True:
    for n in range(1, N+1):
        if arr_dfs[V][n] and not visited_dfs[n]:
            stack.append(V)
            visited_dfs[n] = True
            rst_dfs.append(n)
            V = n
            break
    else:
        if stack:
            V = stack.pop()
        else:
            break

while queue:
    var = queue.pop(0)
    if visited_bfs[var]:
        continue
    else:
        visited_bfs[var] = True
        rst_bfs.append(var)
    for num in arr_bfs[var]:
        queue.append(num)

print(*rst_dfs)
print(*rst_bfs)