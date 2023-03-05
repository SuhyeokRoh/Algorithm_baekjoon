for _ in range(4):
    lst = list(map(int, input().split()))
    x1, y1, x2, y2 = lst[:4]
    x3, y3, x4, y4 = lst[4:]


    if (x2 == x3 and y2 == y3) or (x2 == x3 and y1 == y4) or (x4 == x1 and y4 == y1) or (x4 == x1 and y3 == y2):
        print('c')
    elif (x3 > x2) or (y3 > y2) or (x1 > x4) or (y1 > y4):
        print('d')
    elif (x3 == x2) or (y3 == y2) or (x1 == x4) or (y1 == y4):
        print('b')
    else:
        print('a')