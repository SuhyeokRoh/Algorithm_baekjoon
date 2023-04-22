n=int(input())
lst = list(map(int, input().split()))
cnt = 0
for x in lst:
    if x == n:
        cnt += 1
print(cnt)