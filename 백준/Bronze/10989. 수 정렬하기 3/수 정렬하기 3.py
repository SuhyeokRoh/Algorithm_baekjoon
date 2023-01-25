import sys

loop = int(sys.stdin.readline())

number = [0] * 10001

for i in range(loop):
    num = int(sys.stdin.readline())
    number[num] += 1

for idx in range(10001):
    if number[idx] != 0:
        while number[idx] > 0:
            print(idx)
            number[idx] -= 1