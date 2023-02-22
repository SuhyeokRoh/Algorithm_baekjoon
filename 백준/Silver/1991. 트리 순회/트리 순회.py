def pre_order(arr, idx):
    if idx < 0 or idx > 25:
        return
    print(chr(idx + 65), end='')
    pre_order(arr, ord(arr[idx][0])-65)
    pre_order(arr, ord(arr[idx][1])-65)


def in_order(arr, idx):
    if idx < 0 or idx > 25:
        return
    in_order(arr, ord(arr[idx][0])-65)
    print(chr(idx + 65), end='')
    in_order(arr, ord(arr[idx][1])-65)


def post_order(arr, idx):
    if idx < 0 or idx > 25:
        return
    post_order(arr, ord(arr[idx][0])-65)
    post_order(arr, ord(arr[idx][1])-65)
    print(chr(idx + 65), end='')


N = int(input())
arr = [[] for _ in range(N)]
rst = [0] * N
for _ in range(N):
    idx, left, right = map(str, input().split())
    arr[ord(idx)-65] = (left, right)

pre_order(arr, 0)
print()
in_order(arr, 0)
print()
post_order(arr, 0)
print()