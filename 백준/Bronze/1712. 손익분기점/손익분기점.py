price = str(input()).split()
a,b,c = list(map(int,price))

if c <= b:
    print(-1)
else:
    x = int(a /(c - b)) + 1
    print(x)