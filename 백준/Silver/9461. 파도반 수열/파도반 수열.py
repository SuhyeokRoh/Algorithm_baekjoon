import sys
lst = [0, 1, 1]
for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    i = len(lst)
    while i < n+1:
        a, b = lst[i-2], lst[i-3]
        lst.append(a + b)
        i += 1
    print(lst[n])