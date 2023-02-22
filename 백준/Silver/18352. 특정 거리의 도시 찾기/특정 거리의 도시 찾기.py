import sys

def distance(arr, idx):
    queue = []
    front = rear = -1
    for number in arr[idx]:
        rear += 1
        rst[number] = rst[idx] + 1
        visited[number] = True
        queue.append(number)
    while front != rear:
        front += 1
        var = queue[front]
        for num in arr[var]:
            if not visited[num]:
                rear += 1
                rst[num] = rst[var] + 1
                visited[num] = True
                queue.append(num)


N, M, K, X = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(N+1)]
rst = [0] * (N+1)
visited = [False] * (N+1)
visited[X] = True
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    arr[start].append(end)

distance(arr, X)
cnt = []
for i in range(2, N+1):
    if rst[i] == K:
        cnt.append(i)

if not cnt:
    print(-1)
else:
    for number in cnt:
        print(number)