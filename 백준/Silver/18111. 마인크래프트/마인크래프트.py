N, M, B = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
maxV = 0

for i in range(N):
    maxV = max(maxV, max(lst[i]))

rst = [987654321, 0]

while maxV >= 0:
    cnt = block = 0
    for i in range(N):
        for j in range(M):
            var = lst[i][j] - maxV
            if var < 0:
                cnt += abs(var)
                block += var
            else:
                cnt += 2 * var
                block += var
    if block < 0 and abs(block) > B:
        maxV -= 1
    elif rst[0] > cnt:
        rst = [cnt, maxV]
        maxV -= 1
    else:
        break

print(*rst)