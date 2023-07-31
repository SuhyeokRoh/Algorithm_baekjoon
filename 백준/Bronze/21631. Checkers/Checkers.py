a,b = map(int, input().split())

c = b - 1
if a >= c:
    print(b)
else:
    print(b - (c - a))