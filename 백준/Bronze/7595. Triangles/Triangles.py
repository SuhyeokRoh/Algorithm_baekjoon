while True:
    num = int(input())
    if not num:
        break
    for i in range(1, num+1):
        print('*'*i)