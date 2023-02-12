import sys

rng = int(sys.stdin.readline())
lst = [0] + list(map(int, sys.stdin.readline().split())) + [1000]
lst.sort()

n = int(sys.stdin.readline())
cnt = 0
if n not in lst:
    for i in range(rng):
        if lst[i] < n and lst[i+1] > n:
            for idx in range(lst[i]+1, n+1):
                for j_idx in range(n, lst[i+1]):
                    if idx != j_idx:
                        cnt += 1

print(cnt)