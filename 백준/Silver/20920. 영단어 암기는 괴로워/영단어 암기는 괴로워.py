import sys

m, n = map(int, sys.stdin.readline().split())
dict = {}

for _ in range(m):
    word = sys.stdin.readline().rstrip()
    if len(word) < n:
        continue
    if dict.get(word):
        dict[word] += 1
    else:
        dict[word] = 1

result = sorted(dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for x in result:
    print(x[0])
