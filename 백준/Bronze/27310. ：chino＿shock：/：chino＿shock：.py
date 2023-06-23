word = input()
a, b = 0, 0
for i in word:
    if i == ":":
        a += 1
    
    if i == "_":
        b += 1

print(len(word)+a+b*5)    