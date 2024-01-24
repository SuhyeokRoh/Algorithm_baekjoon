import sys

q, s, e = [], 0, 0
for _ in range(int(input())):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        q.append(order[-1])
        e += 1
    elif order[0] == "pop":
        if s < e:
            print(q[s])
            s += 1
        else:
            print(-1)
    elif order[0] == "size":
        print(e-s)
    elif order[0] == "empty":
        print(1 if e == s else 0)
    elif order[0] == "front":
        if s < e:
            print(q[s])
        else:
            print(-1)
    else:
        if s < e:
            print(q[-1])
        else:
            print(-1)