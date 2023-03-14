n = int(input())
lst = [i**2 for i in range(int(n**0.5)+1)]
cnt = 0
arr = [n]
while True:
    cnt += 1
    temp = set()
    for number in arr:
        for var in lst:
            if var <= number:
                temp.add(number - var)
        
    if 0 in temp:
        break
    arr = list(temp)

print(cnt)