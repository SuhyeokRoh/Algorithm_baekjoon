import math
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
#
#
# def lcm(a, b):
#     return a * b // gcd(a, b)


n1, a = map(int, input().split())
n2, b = map(int, input().split())

div_m = math.lcm(a,b)
div_s = n1 * (div_m // a) + n2 * (div_m // b)

num = math.gcd(div_m, div_s)
if num > 1:
    div_m //= num
    div_s //= num

# div_m = lcm(a, b)
# div_s = n1 * (div_m // a) + n2 * (div_m // b)
if div_m == div_s:
    print(1, 1)
else:
    print(div_s, div_m)