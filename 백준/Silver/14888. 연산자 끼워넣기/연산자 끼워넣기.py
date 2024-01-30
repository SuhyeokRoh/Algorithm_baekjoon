import sys


def find_min_max(index, used, rst):
    global minV, maxV

    if index == n:
        minV = min(rst, minV)
        maxV = max(rst, maxV)
        return
    else:
        for i in range(4):
            if used[i] < arith[i]:
                used[i] += 1
                if i == 0:
                    find_min_max(index+1, used, rst + numbers[index])
                elif i == 1:
                    find_min_max(index+1, used, rst - numbers[index])
                elif i == 2:
                    find_min_max(index+1, used, rst * numbers[index])
                else:
                    if rst < 0:
                        tmp = -rst // numbers[index]
                        find_min_max(index+1, used, -tmp)
                    else:
                        tmp = rst // numbers[index]
                        find_min_max(index+1, used, tmp)
                used[i] -= 1


n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
arith = list(map(int, sys.stdin.readline().split()))
minV, maxV = int(1e9), int(-1e9)
find_min_max(1, [0, 0, 0, 0], numbers[0])
print(maxV)
print(minV)