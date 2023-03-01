num = {1:0, 0:1}
switch = int(input())

lst = [-1] + list(map(int, input().split()))
student = int(input())

for _ in range(student):
    gender, number = map(int, input().split())
    if gender == 1:
        for i in range(number, len(lst), number):
            lst[i] = num[lst[i]]
    else:
        idx = [number]
        l_idx, r_idx = number-1, number+1
        while l_idx >= 1 and r_idx < len(lst):
            if lst[l_idx] == lst[r_idx]:
                idx.append(l_idx)
                idx.append(r_idx)
            else:
                break
            l_idx -= 1
            r_idx += 1
        for n in idx:
            lst[n] = num[lst[n]]
            
lst = lst[1:]

if len(lst) <= 20:
    print(*lst)
else:
    while len(lst):
        for _ in range(20):
            if not lst:
                break
            print(lst.pop(0), end= ' ')
        if not lst:
            break
        print()
