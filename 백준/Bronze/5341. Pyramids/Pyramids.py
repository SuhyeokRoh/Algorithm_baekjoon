while True:
    n = int(input())
    if not n:
        break
    print(sum(list(range(1, n+1))))