word = input()
rst = 0
for i in range(len(word)-3):
    if word[i:i+4] == 'DKSH':
        rst += 1
print(rst)