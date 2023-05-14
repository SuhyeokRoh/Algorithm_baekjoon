lst = list(input())
a, b = 0, 0
if lst[0] == '1' and lst[1] == '0':
    a = 10
else:
    a = int(lst[0])

if len(lst) >= 3:
    if lst[1] == '0':
        if len(lst) == 4:
            b = 10
        else:
            b = int(lst[2])
    else:
        b = 10
else:
    b = int(lst[1])

print(a+b)