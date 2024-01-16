n = int(input())
result, i = 0, 1
while True:
    if i ** 2 <= n:
        result += 1
        i += 1
    else:
        break
print(result)
