import sys

n = int(sys.stdin.readline().rstrip())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
minimum = price.index(min(price[:-1]))
rst, index = 0, 0

while index < n:
    if index == minimum:
        rst += sum(distance[index:n-1]) * price[index]
        break
    else:
        i = 1
        while price[index] < price[index+i] and index + i != minimum:
            i += 1
        rst += sum(distance[index:index+i]) * price[index]
        index += i
print(rst)
