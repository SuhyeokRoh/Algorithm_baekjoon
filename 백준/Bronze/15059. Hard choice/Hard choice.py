a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
rst = 0
if a1 < a2:
    rst += a2 - a1
if b1 < b2:
    rst += b2 - b1
if c1 < c2:
    rst += c2 - c1
print(rst)