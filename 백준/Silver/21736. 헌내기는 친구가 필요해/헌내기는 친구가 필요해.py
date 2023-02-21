row, col = map(int, input().split())
arr = [['X'] + list(input()) + ['X'] for _ in range(row)]
arr = [['X'] * (col+2)] + arr + [['X'] * (col+2)]
visited = [[False] * (col+2) for _ in range(row+2)]

start, front, rear, cnt = 0, -1, 0, 0
for i in range(1, row+1):
    for j in range(1, col+1):
        if arr[i][j] == 'I':
            start = (i, j)
            break
    if start:
        break

queue = [start]
delta_move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while front != rear:
    front += 1
    i, j = queue[front]
    for x, y in delta_move:
        if arr[i+x][j+y] == 'O' and not visited[i+x][j+y]:
            rear += 1
            queue.append((i+x, j+y))
            visited[i + x][j + y] = True
        elif arr[i+x][j+y] == 'P' and not visited[i+x][j+y]:
            cnt += 1
            rear += 1
            queue.append((i+x, j+y))
            visited[i + x][j + y] = True

if not cnt: print('TT')
else: print(cnt)