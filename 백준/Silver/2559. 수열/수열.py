N, K = map(int, input().split())
lst = list(map(int, input().split()))
total = sum(lst[:K])
rst = total

for i in range(N-K):
    total = total - lst[i] + lst[i+K]
    rst = max(rst, total)
print(rst)