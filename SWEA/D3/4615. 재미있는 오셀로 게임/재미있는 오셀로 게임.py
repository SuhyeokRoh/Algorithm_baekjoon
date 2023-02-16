for case in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[3] + [0] * N + [3] for _ in range(N)]
    arr = [[3] * (N+2)] + arr + [[3] * (N+2)]

    for i in range(2):
        arr[(N+2)//2-i][(N+2)//2-i] = 2
        arr[((N+2)//2-1)+i][(N+2)//2-i] = 1

    xy_move = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for _ in range(M):
        a, b, color = map(int, input().split())
        if color == 1:
            arr[b][a] = 1
            lst = []
            for y, x in xy_move:
                if arr[b+x][a+y] == 2:
                    c = b + x
                    d = a + y
                    while arr[c][d] == 2:
                        lst.append([c,d])
                        c += x
                        d += y
                    if arr[c][d] == 1:
                        for i, j in lst:
                            arr[i][j] = 1
                    else:
                        lst.clear()
            else:
                continue
        else:
            arr[b][a] = 2
            lst = []
            for y, x in xy_move:
                if arr[b+x][a+y] == 1:
                    c = b + x
                    d = a + y
                    while arr[c][d] == 1:
                        lst.append([c,d])
                        c += x
                        d += y
                    if arr[c][d] == 2:
                        for i, j in lst:
                            arr[i][j] = 2
                    else:
                        lst.clear()
            else:
                continue
    cnt_black = cnt_white = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                cnt_black += 1
            elif arr[i][j] == 2:
                cnt_white += 1

    print('#{} {} {}'.format(case, cnt_black, cnt_white))