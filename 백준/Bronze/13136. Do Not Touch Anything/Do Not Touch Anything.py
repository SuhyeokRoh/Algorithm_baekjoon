a,b,c = map(int, input().split())
d, e = a // c, b // c
if (a % c):
    d += 1
if (b % c):
    e += 1
print(d*e)