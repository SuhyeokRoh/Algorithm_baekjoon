import sys
sys.setrecursionlimit(10**6)

def find_upper_node(lst, number, idx):

    if not lst:
        return

    else:
        rst[number] = idx
        while lst:
            var = lst.pop()
            if var == idx:
                continue
            find_upper_node(arr[var], var, number)


node = int(input())
arr = [[] for _ in range(node+1)]
rst = [0] * (node+1)

for _ in range(node-1):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

for number in arr[1]:
    find_upper_node(arr[number], number, 1)

for idx in range(2, node+1):
    print(rst[idx])
