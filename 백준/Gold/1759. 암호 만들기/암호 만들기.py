L, C = map(int, input().split())
word = list(input().split())
rst = []


def make_pwd(cnt):

    if cnt == C - L:
        temp = []
        cnt_v = cnt_c = 0
        for k in range(len(word)):
            if k in idx:
                continue
            else:
                if word[k] in 'aeiou':
                    cnt_v += 1
                else:
                    cnt_c += 1
                temp.append(word[k])
        if cnt_v < 1 or cnt_c < 2:
            return
        else:
            temp.sort()
            rst.append(''.join(temp))

    else:
        for j in range(idx[-1], len(word)):
            if j in idx:
                continue
            else:
                idx.append(j)
                make_pwd(cnt+1)
                idx.remove(j)


if L == C:
    word.sort()
    rst.append(''.join(word))

else:
    for i in range(C):
        idx = [i]
        make_pwd(1)

rst.sort()

for w in rst:
    print(w)