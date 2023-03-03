lst, result = [], []
for _ in range(9):
    lst.append(int(input()))
lst.sort()
val = sum(lst)

for i in range(8):
    for j in range(i+1, 9):
         if val - (lst[i] + lst[j]) == 100:
             result = [i, j]
             break

for idx in range(9):
    if idx in result:
        continue
    print(lst[idx])
