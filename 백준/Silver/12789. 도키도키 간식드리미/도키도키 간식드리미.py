import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
stack = []
i, number, rst = 0, 1, 1
while True:
    if i < n:
        stack.append(lst[i])
        i += 1

    if i == n and len(stack) == 0:
        break

    if stack[-1] == number:
        while len(stack) != 0 and stack[-1] == number:
            stack.pop()
            number += 1
    else:
        if i < n:
            continue
        else:
            if stack:
                rst = 0
                break
print("Nice" if rst == 1 else "Sad")
