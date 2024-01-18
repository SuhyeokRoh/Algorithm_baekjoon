from itertools import combinations
n,m = map(int, input().split())
rst = list(combinations([str(x) for x in range(1, n+1)], m))
print('\n'.join(' '.join(x) for x in rst))