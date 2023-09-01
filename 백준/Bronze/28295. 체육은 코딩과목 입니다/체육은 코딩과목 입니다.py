rst = 0
for _ in range(10):
    i = int(input())
    rst += i * 90
rst = (rst // 90) % 4

if rst == 0:
    print("N")
elif rst == 1:
    print("E")
elif rst == 2:
    print("S")
else:
    print("W")