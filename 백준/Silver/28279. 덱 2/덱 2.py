from collections import deque
import sys


def order(lst, deq):
    if lst[0] == "1":
        deq.appendleft(lst[1])
    elif lst[0] == "2":
        deq.append(lst[1])
    elif lst[0] == "3":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif lst[0] == "4":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif lst[0] == "5":
        print(len(deq))
    elif lst[0] == "6":
        print(0 if q else 1)
    elif lst[0] == "7":
        print(deq[0] if deq else -1)
    else:
        print(deq[-1] if deq else -1)


q = deque([])
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    sentence = sys.stdin.readline().split()
    order(sentence, q)