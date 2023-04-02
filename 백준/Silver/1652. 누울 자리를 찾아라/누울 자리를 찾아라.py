N = int(input())
arr = [list(input()) for _ in range(N)]
lst = [0] * 2
for i in range(N):
    height = width = 0
    for j in range(N):
        if arr[i][j] == 'X':
            if width >= 2:
                lst[0] += 1
            width = 0
        else:
            width += 1

        if arr[j][i] == 'X':
            if height >= 2:
                lst[1] += 1
            height = 0
        else:
            height += 1
    if width >= 2:
        lst[0] += 1
    if height >= 2:
        lst[1] += 1
print(*lst)