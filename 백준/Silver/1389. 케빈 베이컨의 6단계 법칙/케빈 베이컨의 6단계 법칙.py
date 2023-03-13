from collections import deque

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
rst = [[0, 0] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for idx in range(1, N+1):
    cnt = 0
    for num in range(1, N+1):
        if idx == num:
            continue
        else:
            visited = [False] * (N+1)
            visited[idx] = True
            q = deque()
            q.append([idx, 0])
            while q:
                people, var = q.popleft()
                if people == num:
                    cnt += var
                    break
                for i in arr[people]:
                    if visited[i]:
                        continue
                    else:
                        q.append([i, var+1])
                        visited[i] = True
    rst[idx] = [cnt, idx]

rst.sort(key=lambda x: (x[0], x[1]))
print(rst[1][1])