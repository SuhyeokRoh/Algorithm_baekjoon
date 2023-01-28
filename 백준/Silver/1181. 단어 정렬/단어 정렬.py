loop = int(input())
word = []
i = 0

for n in range(loop):
    w = input()
    if w in word:
        pass
    else:
        word.append(w)

word.sort()
word.sort(key=len)

for char in word:
    print(char)