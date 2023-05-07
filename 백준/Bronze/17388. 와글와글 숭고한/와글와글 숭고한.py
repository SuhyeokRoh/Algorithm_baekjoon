score = list(map(int, input().split()))

if sum(score) >= 100:
    print("OK")
else:
    if score.index(min(score)) == 0:
        print("Soongsil")
    elif score.index(min(score)) == 1:
        print("Korea")
    else:
        print("Hanyang")