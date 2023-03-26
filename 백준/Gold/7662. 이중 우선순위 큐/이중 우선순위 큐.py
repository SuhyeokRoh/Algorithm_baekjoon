import heapq
import sys

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    h1, h2 = [], []
    visited = [False] * k
    for key in range(k):
        order, number = sys.stdin.readline().split()
        if order == 'I':
            heapq.heappush(h1, (int(number), key))
            heapq.heappush(h2, (-int(number), key))
            visited[key] = True
        else:
            if number == '1':
                while h2 and not visited[h2[0][1]]:
                    heapq.heappop(h2)
                if h2:
                    visited[h2[0][1]] = False
                    heapq.heappop(h2)
            else:
                while h1 and not visited[h1[0][1]]:
                    heapq.heappop(h1)
                if h1:
                    visited[h1[0][1]] = False
                    heapq.heappop(h1)

    while h1 and not visited[h1[0][1]]:
        heapq.heappop(h1)
    while h2 and not visited[h2[0][1]]:
        heapq.heappop(h2)

    if not h1 or not h2:
        print('EMPTY')
    else:
        print(-h2[0][0], h1[0][0])