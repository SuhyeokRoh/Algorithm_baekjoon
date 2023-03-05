w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
x, y = (t - (w - p)), (t - (h - q))
if (x // w) % 2 == 1:
    rst_x = x % w
else:
    rst_x = w - x % w

if (y // h) % 2 == 1:
    rst_y = y % h
else:
    rst_y = h - y % h

print(rst_x, rst_y)