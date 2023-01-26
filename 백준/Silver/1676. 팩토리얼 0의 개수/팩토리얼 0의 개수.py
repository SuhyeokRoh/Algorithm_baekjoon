import sys, math

number = int(sys.stdin.readline())

fact = math.factorial(number)
fact =str(fact)
cnt = 0

for idx in range(len(fact)-1,-1,-1):
    if int(fact[idx]) == 0:
        cnt += 1
    else:
        break
print(cnt)