num = int(input())
cnt, i = 0, 0

while num > cnt:
    i += 1
    cnt += i

if i % 2 == 0:
    print('{}/{}'.format(i-(cnt-num),1+(cnt-num)))
else:
    print('{}/{}'.format(1+(cnt-num),i-(cnt-num)))