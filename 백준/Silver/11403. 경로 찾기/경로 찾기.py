from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
tree = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            tree[i].append(j)

rst = [[0] * N for _ in range(N)]
d = deque()

for i in range(N):
    for j in range(N):
        var = 0
        d.append(i)
        visited = [False] * N
        while d:
            idx = d.popleft()
            if idx == j and visited[idx]:
                var = 1
                d.clear()
                break
            if tree[idx]:
                for x in tree[idx]:
                    if not visited[x]:
                        d.append(x)
                        visited[x] = True
        rst[i][j] = var

for li in rst:
    print(*li)