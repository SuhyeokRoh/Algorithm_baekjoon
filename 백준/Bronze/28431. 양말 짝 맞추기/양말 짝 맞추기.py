rst = []
for _ in range(5):
    a = int(input())
    if a in rst:
        rst.remove(a)
    else:
        rst.append(a)
print(rst[0])