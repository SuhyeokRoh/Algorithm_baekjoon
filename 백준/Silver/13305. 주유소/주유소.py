import sys

n = int(sys.stdin.readline().rstrip())
distance = list(map(int, sys.stdin.readline().split()))
city = list(map(int, sys.stdin.readline().split()))
minV, maxV = city.index(min(city[:-1])), city.index(max(city[:-1]))
x, price = 0, 0

while True:
    if x == minV:
        price += city[x] * sum(distance[x:])
        break
    elif x == maxV:
        price += city[x] * distance[x]
        x += 1
    else:
        tmp = city.index(min(city[x+1:-1]))
        price += city[x] * sum(distance[x:tmp])
        x = tmp

print(price)
