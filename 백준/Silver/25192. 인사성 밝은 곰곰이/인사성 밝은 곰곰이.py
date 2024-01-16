import sys

name, rst = {}, 0

for _ in range(int(input())):
    chat = sys.stdin.readline().split()[0]
    if chat == 'ENTER':
        rst += len(name.keys())
        name.clear()
    else:
        name[chat] = 1
print(rst + len(name.keys()))
