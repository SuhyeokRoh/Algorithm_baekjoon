number, _ = map(int, input().split())
lst, cnt = [], 0
result = ''
for _ in range(number):
    word = list(input())
    lst.append(word)
for arr in zip(*lst):
    dic = {'A' : 0, 'T' : 0, 'C' : 0, 'G' : 0}
    for spell in arr:
        dic[spell] += 1
    maxV = max(dic.values())
    name = [k for k,v in dic.items() if v == maxV]
    name.sort()
    cnt += number - dic[name[0]]
    result += name[0]

print(result)
print(cnt)