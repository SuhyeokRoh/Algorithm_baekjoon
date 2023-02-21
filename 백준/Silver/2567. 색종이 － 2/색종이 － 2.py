arr = [[0] * 101 for _ in range(101)]
for _ in range(int(input())):
    left, downward = map(int, input().split())
    for i in range(downward, downward+10):
        for j in range(left, left+10):
            arr[i][j] = 1

delta_move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
rectangle_perimeter = 0

for i in range(101):
    for j in range(101):
        if not arr[i][j]:
            continue
        else:
            for x, y in delta_move:
                a = i + x
                b = j + y
                if not arr[a][b]:
                    rectangle_perimeter += 1

print(rectangle_perimeter)