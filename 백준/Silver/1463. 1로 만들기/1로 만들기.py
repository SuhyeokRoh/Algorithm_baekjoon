def Dynamic_Prog(number):
    f = [0]

    for i in range(2, number+1):
        a = b = c = 987654321
        if not i % 3:
            a = f[i//3-1] + 1
        if not i % 2:
            b = f[i//2-1] + 1
        c = f[i-2] + 1
        f.append(min(a,b,c))

    return f[number-1]

print(Dynamic_Prog(int(input())))