import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
arr, var = [0], 0
for num in lst:
    var += num
    arr.append(var)

for _ in range(M):
    start, end = map(int, input().split())
    print(arr[end] - arr[start-1])