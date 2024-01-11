import sys
dict = {}
for _ in range(int(sys.stdin.readline().split()[0])):
    name, state = sys.stdin.readline().split()
    if dict.get(name):
        dict[name] = (dict[name] + 1) % 2
    else:
        dict[name] = 1
result = [k for k, v in dict.items() if v]
result.sort(reverse=True)
print(*result, sep='\n')