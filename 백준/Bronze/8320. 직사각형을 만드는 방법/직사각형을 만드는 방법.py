number = int(input())
idx = 2
rst = number
while True:
    var = number // idx
    if var <= idx - 1:
        break
    rst += var - (idx - 1)
    idx += 1
print(rst)