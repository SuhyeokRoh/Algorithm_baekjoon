N, K = map(int, input().split())
price = []
for _ in range(N):
    price.append(int(input()))
price.sort(reverse=True)

cnt = 0
for idx in range(N):
    cnt += K // price[idx]
    K %= price[idx]
print(cnt)
