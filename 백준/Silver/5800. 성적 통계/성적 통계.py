for idx in range(1, int(input())+1):
    n = list(map(int, input().split()))
    l, score = n[0], n[1:]
    score.sort(reverse=True)
    maxV = 0
    for i in range(1, l):
        if maxV < (score[i-1] - score[i]):
            maxV = score[i-1] - score[i]
    print(f'Class {idx} \nMax {score[0]}, Min {score[-1]}, Largest gap {maxV}')