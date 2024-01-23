def recur(rst, x, start):
    if x == 0:
        return
    else:
        s = start + 3**(x-1)
        for i in range(3**(x-1)):
            rst[s+i] = 0
        recur(rst, x-1, start)
        recur(rst, x-1, s+3**(x-1))
    return


while True:
    try:
        n = int(input())
        lst = [1 for x in range(3**n)]
        recur(lst, n, 0)
        print(''.join('-' if i == 1 else ' ' for i in lst))
    except:
        break