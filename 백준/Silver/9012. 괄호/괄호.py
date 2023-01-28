loop = int(input())

for case in range(loop):
    word = input()
    cnt = 0
    for w in word:
        if w == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                break
    if cnt == 0:
        print('YES')
    else:
        print('NO')