word = list(input())
lst = [0] * 26
for x in word:
    lst[ord(x)-97] += 1
print(*lst)