while True:
    num = int(input())
    if num == 0:
        break
    maxv = 2 * num
    find_prime, dif_num = list(range(num+1,maxv+1)), []
    dble = 1
    while maxv >= dble * dble:
        dble += 1
    for number in range(2,dble):
        for div_num in range(int(num/number),int(maxv/number)+1):
            dif_num.append(number * div_num)
    result = len(set(find_prime) - set(dif_num))
    print(result)