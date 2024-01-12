import sys


def gcd(x, y):
    if x < y:
        x, y = y, x

    if y == 0:
        return x

    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


def lcm(x, y):
    value = gcd(x, y)
    return x * y // value


a, b = map(int, sys.stdin.readline().split())
print(lcm(a, b))