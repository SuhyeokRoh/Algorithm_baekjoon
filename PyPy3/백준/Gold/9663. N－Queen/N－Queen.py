def queen(i, n, lst):
    global rst

    if i == n - 1:
        rst += lst[i].count(0)
        return

    for x in range(n):
        if lst[i][x] == 0:
            t, tmp = 0, []
            while i+t < n:
                if lst[i+t][x] == 0:
                    lst[i+t][x] = 1
                    tmp.append([i+t, x])
                if x-t >= 0 and lst[i+t][x-t] == 0:
                    lst[i+t][x-t] = 1
                    tmp.append([i+t, x-t])
                if x+t < n and lst[i+t][x+t] == 0:
                    lst[i+t][x+t] = 1
                    tmp.append([i+t, x+t])
                t += 1
            queen(i+1, n, lst)
            for j, k in tmp:
                lst[j][k] = 0
        else:
            continue

rst = 0
n = int(input())
lst = [[0] * n for _ in range(n)]
queen(0, n, lst)
print(rst)