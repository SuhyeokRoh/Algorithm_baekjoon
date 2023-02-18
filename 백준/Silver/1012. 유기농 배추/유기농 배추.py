for case in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0]*(M+2) for _ in range(N+2)]
    visit = [[False] * (M+2) for _ in range(N+2)]
    stack = []

    for _ in range(K):
        i, j = map(int, input().split())
        arr[j+1][i+1] = 1

    movement = [[1,0], [0,1], [-1,0], [0,-1]]
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if visit[i][j]:
                continue
            elif arr[i][j]:
                visit[i][j] = True
                while True:
                    for x, y in movement:
                        if arr[i+x][j+y] and not visit[i+x][j+y]:
                            stack.append((i,j))
                            i += x
                            j += y
                            visit[i][j] = True
                            break
                    else:
                        if stack:
                            i, j = stack.pop()
                        else:
                            cnt += 1
                            break
    print(cnt)