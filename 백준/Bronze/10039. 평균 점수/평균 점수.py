rst = 0
for _ in range(5):
    n = int(input())
    if n < 40:
        rst += 40
    else:
        rst += n
print(rst//5)