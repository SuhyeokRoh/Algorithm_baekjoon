import sys


def gcd(m, n):
    if m < n:
        m, n = n, m

    if n == 0:
        return m

    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


tree = []
distance = []
n = int(sys.stdin.readline().split()[0])

for i in range(n):
    tree.append(int(sys.stdin.readline().split()[0]))
    if i > 0:
        distance.append(tree[i] - tree[i-1])

s, result = distance[0], 0

for i in range(1, len(distance)):
    s = gcd(s, distance[i])

for i in range(1, len(tree)):
    result += ((tree[i] - tree[i-1]) // s) - 1
print(result)