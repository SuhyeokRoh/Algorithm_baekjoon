while True:
    w, h = map(int, input().split())
    if w == 0 or h == 0:
        break
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(h)]
    arr = [[0] * (w+2)] + arr + [[0] * (w+2)]
    visit = [[False] * (w+2) for _ in range(h+2)]
    stack = []
    cnt = 0

    movement = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
    for i in range(1, h+1):
        for j in range(1, w+1):
            if visit[i][j]:
                continue
            if arr[i][j] and not visit[i][j]:
                a = i
                visit[a][j] = True
                while True:
                    for x, y in movement:
                        if arr[a+x][j+y] and not visit[a+x][j+y]:
                            stack.append((a, j))
                            a += x
                            j += y
                            visit[a][j] = True
                            break
                    else:
                        if stack:
                            a, j = stack.pop()
                        else:
                            cnt += 1
                            break

    print(cnt)
