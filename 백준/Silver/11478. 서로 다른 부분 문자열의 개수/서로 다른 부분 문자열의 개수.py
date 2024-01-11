import sys

word = sys.stdin.readline()
li = []
for i in range(1, len(word)):
    for j in range(len(word) - i):
        li.append(word[j:j+i])
print(len(set(li)))