A,B = 0, 0
for i in range(6):
    number = int(input())
    if i // 3 == 0:
        if i % 3 == 0:
            A += 3 * number
        elif i % 3 == 1:
            A += 2 * number
        else:
            A += number
    else:
        if i % 3 == 0:
            B += 3 * number
        elif i % 3 == 1:
            B += 2 * number
        else:
            B += number
if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("T")