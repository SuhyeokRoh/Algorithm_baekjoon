from itertools import combinations

n = int(input())
maxV = [0, 0]
for i in range(n):
    lst = list(map(int, input().split()))
    for x in list(combinations(lst, 3)):
        tmp = sum(x)
        if maxV[0] <= tmp % 10:
            maxV = [tmp%10, i+1]
print(maxV[-1])