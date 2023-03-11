from collections import deque

start, end = map(int, input().split())
visited = [False] * 100001
visited[start] = True
q = deque()
q.append((start, 0))
rst = 0

while q:
    num, cnt = q.popleft()
    if num == end:
        rst = cnt
        break

    for var in (num-1, num+1, num*2):
        if 0 <= var <= 100000 and not visited[var]:
            q.append((var, cnt+1))
            visited[var] = True

print(rst)