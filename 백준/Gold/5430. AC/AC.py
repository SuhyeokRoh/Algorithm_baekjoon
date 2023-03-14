from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    order = list(map(str, input().rstrip()))
    n = int(input())
    arr = ((input().rstrip()).lstrip('['))
    rst, direction = 1, 0
    if not n:
        arr = deque()
    else:
        arr = arr[:-1]
        arr = deque(map(int, arr.split(',')))

    for odr in order:
        if odr == 'R':
            direction = (direction + 1) % 2
        else:
            if not direction:
                if arr:
                    arr.popleft()
                else:
                    rst = 0
                    break
            else:
                if arr:
                    arr.pop()
                else:
                    rst = 0
                    break

    if not rst:
        print('error')
    else:
        if arr:
            if direction:
                arr.reverse()
            print(str(list(arr)).replace(' ', ''))
        else:
            print('[]')