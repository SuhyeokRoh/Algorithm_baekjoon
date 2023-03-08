import sys

computer = int(sys.stdin.readline())
tree = [[] for _ in range(computer+1)]
infection = [False] * (computer + 1)
infection[1] = True
for _ in range(int(sys.stdin.readline())):
    num1, num2 = map(int, sys.stdin.readline().split())
    tree[num1].append(num2)
    tree[num2].append(num1)

q = [1]
front, rear, cnt = -1, 0, 0
while front != rear:
    front += 1
    idx = q[front]
    if not tree[idx]:
        continue
    else:
        for num in tree[idx]:
            if infection[num]:
                continue
            rear += 1
            cnt += 1
            q.append(num)
            infection[num] = True

print(cnt)