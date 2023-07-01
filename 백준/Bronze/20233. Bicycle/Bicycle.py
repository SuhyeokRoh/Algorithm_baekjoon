a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

if t >= 30:
    a += ((t - 30) * x) * 21
if t >= 45:
    b += ((t - 45) * y) * 21
    
print(a,b)