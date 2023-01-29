M = int(input())
N = int(input())
PN = list(range(M,N+1,1))

for num in range(N-M+1):
    num += M
    if num == 1:
        PN.remove(num)
    for dv in range(2, int(num/2)+1):
        if num % dv == 0:
            PN.remove(num)
            break

if len(PN) == 0:
    print(-1)
else:
    print(sum(PN))
    print(PN[0])