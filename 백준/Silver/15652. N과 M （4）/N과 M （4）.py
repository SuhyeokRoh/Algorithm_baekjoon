import sys


def overlap_per(rst, x):

    if x == m:
        print(' '.join(''.join(str(x)) for x in rst))

    else:
        for j in lst:
            if rst[-1] <= j:
                overlap_per(rst + [j], x+1)


n, m = map(int, sys.stdin.readline().split())
lst = list(x for x in range(1, n+1))
for i in lst:
    overlap_per([i], 1)