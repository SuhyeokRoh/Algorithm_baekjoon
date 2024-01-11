import sys
_ = sys.stdin.readline()
number = {}
for x in sys.stdin.readline().split():
    number[x] = 1
for y in sys.stdin.readline().split():
    if number.get(y):
        number[y] = 0
    else:
        number[y] = 1
result = [k for k, v in number.items() if v]
print(len(result))