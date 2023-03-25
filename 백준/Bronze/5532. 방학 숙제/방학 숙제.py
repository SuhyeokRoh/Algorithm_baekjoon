L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
a, b = divmod(A, C)
c, d = divmod(B, D)
if b:
    a += 1
if d:
    c += 1
print(L-max(a,c))