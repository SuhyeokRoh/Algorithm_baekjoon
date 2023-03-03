paper = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for i in range(1, paper+1):
    x, y, width, height = map(int, input().split())
    for idx in range(height):
        for jdx in range(width):
            arr[y+idx][x+jdx] = i

for num in range(1, paper+1):
    cnt = 0
    for row in range(1001):
        cnt += arr[row].count(num)
    print(cnt)