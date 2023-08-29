for _ in range(int(input())):
    a,b = map(int, input().split())
    a += ((b//4) - (b//7))
    print(a)