import sys

input = sys.stdin.readline

cnt_0 = [1, 0]
cnt_1 = [0, 1]

for case in range(int(input())):
    number = int(input())
    for i in range(len(cnt_0), number+1):
        cnt_0.append(cnt_0[i-1] + cnt_0[i-2])
        cnt_1.append(cnt_1[i-1] + cnt_1[i-2])
    print(cnt_0[number], cnt_1[number])