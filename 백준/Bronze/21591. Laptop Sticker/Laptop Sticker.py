a,b,c,d = map(int, input().split())

if a - c >= 2:
    if b -d >= 2:
        print(1)
    else:
        print(0)
else:
    print(0)