while True:
    a, b = map(int, input().split())
    if not a or not b:
        break
    if a > b:
        print('Yes')
    else:
        print('No')