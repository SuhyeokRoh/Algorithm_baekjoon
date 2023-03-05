for case in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    lst = []
    for i in range(N-1, 0, -1):
        for j in range(i-1, -1, -1):
            lst.append(arr[i] * arr[j])
    lst.sort(reverse=True)

    for num in lst:
        rst = num
        end = num % 10

        while True:
            num //= 10
            before = num % 10
            if before > end:
                rst = -1
                break
            end = before
            if num < 10:
                break

        if rst != -1:
            break

    print(f'#{case} {rst}')