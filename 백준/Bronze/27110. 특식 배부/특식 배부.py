chicken = int(input())
lst = list(map(int, input().split()))
rst = 0

for x in lst:
    if x <= chicken:
        rst += x
    else:
        rst += chicken
print(rst)