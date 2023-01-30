N, K = map(int,input().split())

if K == 0:
    print(1)
else:
    for num in range(N-1,N-K,-1):
        N *= num
    lst = list(range(1,K+1,1))
    total = 1

    for i in lst:
        total *= i

    print(int(N/total))