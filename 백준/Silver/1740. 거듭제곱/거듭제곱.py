N = int(input())
binary_value = list(map(int, bin(N)[2:]))
rst = 0
for i in range(len(binary_value)):
    rst += binary_value[len(binary_value) - 1 - i] * 3 ** i
print(rst)