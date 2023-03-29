min_ham = min_drk = 987654321
for _ in range(3):
    hbg = int(input())
    min_ham = min(min_ham, hbg)

for _ in range(2):
    drink = int(input())
    min_drk = min(min_drk, drink)
print(min_ham + min_drk - 50)