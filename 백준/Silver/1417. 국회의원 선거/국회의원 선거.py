import heapq

n = int(input())
one = int(input())
cnt = 0
heap = []
for _ in range(n-1):
    heapq.heappush(heap, -int(input()))

while heap:
    candidate = -heapq.heappop(heap)
    if one <= candidate:
        one += 1
        cnt += 1
        candidate -= 1
        if one <= candidate:
            heapq.heappush(heap, -candidate)
print(cnt)