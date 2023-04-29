apple1, orange1 = map(int, input().split())
apple2, orange2 = map(int, input().split())
print(min(apple1+orange2, apple2+orange1))