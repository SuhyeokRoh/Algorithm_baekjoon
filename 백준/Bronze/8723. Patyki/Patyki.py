lst = list(map(int, input().split()))
rst = [0, 0, 0]
for i in range(len(lst)):
    rst[i] = lst[i] ** 2

if rst[0] + rst[1] == rst[2] or rst[0] + rst[2] == rst[1] or rst[2] + rst[1] == rst[0]:
    print(1)
elif lst[0] == lst[1] and lst[1] == lst[2]:
    print(2)
else:
    print(0)