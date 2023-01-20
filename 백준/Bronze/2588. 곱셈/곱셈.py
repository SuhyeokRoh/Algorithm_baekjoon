a = int(input())
b = int(input())
c = b // 100
d = (b%100) // 10
e = ((b%100)%10) // 1
print(a*e)
print(a*d)
print(a*c)
print(a*b)