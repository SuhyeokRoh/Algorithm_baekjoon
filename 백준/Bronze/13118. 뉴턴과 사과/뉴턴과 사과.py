lst = list(map(int, input().split()))
position = list(map(int, input().split()))

if position[0] in lst:
    print(lst.index(position[0])+1)
else:
    print(0)