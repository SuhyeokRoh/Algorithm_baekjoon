def make_array(li):
    result = []
    for i in range(6):
        if i in li:
            continue
        result.append(i)
    return result


def ban_index(num):
    var = 6 - num
    if var == 6 or var == 1:
        return var - 1
    elif var % 2 == 1:
        if num == 1:
            return 3
        else:
            return 1
    else:
        if num == 2:
            return 4
        else:
            return 2


def find_max_value(array):
    for i in array:
        var = arr[0][idx]
        end = arr[0][i]
        for j in range(1, dice):
            ind = arr[j].index(end)
            first = arr[j][ban_index(ind)]
            maxV = 0
            for k in range(6):
                if arr[j][k] == first or arr[j][k] == end:
                    continue
                if maxV < arr[j][k]:
                    maxV = arr[j][k]
            var += maxV
            end = first
        lst.append(var)


dice = int(input())
arr = [[] for _ in range(dice)]
for i in range(dice):
    arr[i] = list(map(int, input().split()))
rst, idx = [], 0
while idx < 6:
    lst = []
    num = 6 - idx
    if num == 6 or num == 1:
        ary = make_array([0, 5])
        find_max_value(ary)
    elif num % 2 == 1:
        ary = make_array([1, 3])
        find_max_value(ary)
    else:
        ary = make_array([2, 4])
        find_max_value(ary)
    rst.append(max(lst))
    idx += 1

print(max(rst))