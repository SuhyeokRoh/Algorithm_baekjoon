N, M = map(int, input().split())
lst = list(map(int, input().split()))
start, end = 0, max(lst)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for num in lst:
        if num < mid:
            continue
        cnt += num - mid

    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)