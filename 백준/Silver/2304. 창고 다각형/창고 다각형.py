N = int(input())
arr = [[0, 0] for _ in range(N)]
for i in range(N):
    lst = list(map(int, input().split()))
    arr[i] = lst
arr.sort(key=lambda x: x[0])
maxV = max(arr, key=lambda x: (x[1], x[0]))
end = arr.index(maxV)
place, height, rst = arr[0][0], arr[0][1], maxV[1]
for idx in range(1, end+1):
    if max(height, arr[idx][1]) > height:
        rst += (arr[idx][0] - place) * height
        place, height = arr[idx][0], arr[idx][1]
    else:
        rst += (arr[idx][0] - place) * height
        place = arr[idx][0]

place, height = arr[N-1][0], arr[N-1][1]
for idx in range(N-2, end-1, -1):
    if max(height, arr[idx][1]) > height:
        rst += (place - arr[idx][0]) * height
        place, height = arr[idx][0], arr[idx][1]
    else:
        rst += (place - arr[idx][0]) * height
        place = arr[idx][0]

print(rst)

