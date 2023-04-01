N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

for i in range(N):
    if lst[i][0] == K:
        rst = temp = i
        while temp:
            temp -= 1
            if lst[temp][1:] != lst[rst][1:]:
                break
            else:
                rst -= 1
        print(rst+1)
        break