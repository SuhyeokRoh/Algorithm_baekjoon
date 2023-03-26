N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = [0] * 3


def paper(x, y, N):
    number = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if number != arr[i][j]:
                paper(x, y, N//3)
                paper(x + N//3, y, N//3)
                paper(x + 2*(N//3), y, N//3)
                paper(x, y + N//3, N//3)
                paper(x + N//3, y + N//3, N//3)
                paper(x + 2*(N//3), y + N//3, N//3)
                paper(x, y + 2*(N//3), N//3)
                paper(x + N//3, y + 2*(N//3), N//3)
                paper(x + 2*(N//3), y + 2*(N//3), N//3)
                return
    lst[number] += 1


paper(0,0,N)

for i in range(-1,2,1):
    print(lst[i])