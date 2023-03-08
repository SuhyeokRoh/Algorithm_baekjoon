N = int(input())

lst = list(map(int, input().split()))
lst.sort()
total = 0
for idx in range(N):
    total += lst[idx]
    lst[idx] = total
print(sum(lst))