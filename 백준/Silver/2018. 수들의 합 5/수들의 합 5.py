number = int(input())
cnt, i = 1, 2
while sum(range(1, i+1, 1)) <= number:
    val = number // i
    sumV = sum(list(range(val, val+i, 1)))
    if not abs(number - sumV) % i:
        cnt += 1
    i += 1
print(cnt)
