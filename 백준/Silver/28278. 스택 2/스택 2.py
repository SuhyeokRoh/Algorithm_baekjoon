import sys

n = int(sys.stdin.readline().split()[0])
stack = []

for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    if lst[0] == 1:
        stack.append(lst[1])
    elif lst[0] == 2:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif lst[0] == 3:
        print(len(stack))
    elif lst[0] == 4:
        print(1 if len(stack) == 0 else 0)
    else:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)