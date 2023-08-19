n = int(input())
lst = list(map(int, input().split()))
odd, even = 0, 0
for i in range(n):
    if lst[i] % 2 == 0:
        even += 1
    else:
        odd += 1
if odd >= even:
    print('Sad')
else:
    print("Happy")