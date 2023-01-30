import sys

num1 = int(sys.stdin.readline())
dict = {}
num_list = list(map(int,sys.stdin.readline().split()))

for number in num_list:
    if number in dict.keys():
        dict[number] += 1
    else:
        dict[number] = 1

num2 = int(sys.stdin.readline())
num_list2 = list(map(int,sys.stdin.readline().split()))

for number in num_list2:
    if number in dict.keys():
        print(dict[number], end=' ')
    else:
        print(0, end=' ')