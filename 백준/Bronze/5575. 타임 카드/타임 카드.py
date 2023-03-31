def find_time(A, B):
    start = end = 0
    for x in A:
        start = start * 60 + x
    for y in B:
        end = end * 60 + y
    time = end - start
    rst = []
    for _ in range(2):
        rst = [time % 60] + rst
        time //= 60
    rst = [time] + rst
    print(*rst)


A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_start, A_end = A[:3], A[3:]
B_start, B_end = B[:3], B[3:]
C_start, C_end = C[:3], C[3:]

find_time(A_start, A_end)
find_time(B_start, B_end)
find_time(C_start, C_end)
