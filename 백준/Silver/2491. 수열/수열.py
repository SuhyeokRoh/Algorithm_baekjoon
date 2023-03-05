number = int(input())
arr = list(map(int, input().split()))
lst, cnt = [], 1

for i in range(1, number):
    if arr[i-1] <= arr[i]:
        cnt += 1
    else:
        lst.append(cnt)
        cnt = 1
lst.append(cnt)

cnt = 1
for i in range(number-2, -1, -1):
    if arr[i+1] <= arr[i]:
        cnt += 1
    else:
        lst.append(cnt)
        cnt = 1
lst.append(cnt)

print(max(lst))