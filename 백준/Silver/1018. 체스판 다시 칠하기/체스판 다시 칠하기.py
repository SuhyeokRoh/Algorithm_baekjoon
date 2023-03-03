N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
color = {'W': 'B', 'B': 'W'}
delta = [(1, 0), (0, 1)]
minV = 987654321

for i in range(N-8+1):
    for j in range(M-8+1):
        for val in color.keys():
            cnt = 0
            q = [(i, j, 0)]
            front, rear, diff = -1, 0, 0
            visited = [[False] * 8 for _ in range(8)]
            visited[0][0] = True
            if board[i][j] != val:
                cnt += 1
            val = color[val]
            while front != rear:
                front += 1
                row, col, idx = q[front]
                if diff < idx:
                    val = color[val]
                    diff = idx
                for x, y in delta:
                    if row + x < i + 8 and col + y < j + 8 and not visited[row+x-i][col+y-j]:
                        if val != board[row+x][col+y]:
                            cnt += 1
                        rear += 1
                        visited[row+x-i][col+y-j] = True
                        q.append((row+x, col+y, idx+1))
                if idx == 14 or cnt >= minV:
                    break
            if minV > cnt:
                minV = cnt
if minV == 987654321:
    minV = 0
print(minV)