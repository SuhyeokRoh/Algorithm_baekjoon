import copy

first = int(input())
cnt = 0
compare_list = []
second = first // 2

while second <= first:
    compare_list.append(first)
    compare_list.append(second)
    idx = 0
    while True:
        var = compare_list[idx] - compare_list[idx+1]
        if var < 0:
            break
        compare_list.append(var)
        idx += 1
    if cnt < len(compare_list):
        cnt = len(compare_list)
        rst = copy.deepcopy(compare_list)

    compare_list.clear()
    second += 1

print(cnt)
print(*rst)