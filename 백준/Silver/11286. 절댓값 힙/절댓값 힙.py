import heapq, sys

input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    x = int(input())
    if not x:
        if not heap:
            print('0')
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))