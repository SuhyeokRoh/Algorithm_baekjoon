a,b,c,d,e,f = map(int, input().split())
rst = 0
for x in range(-999, 1000, 1):
    for y in range(-999, 1000, 1):
        if a*x+b*y == c and d*x+e*y == f:
            rst = 1
            print(x, y)
            break
    if rst:
        break