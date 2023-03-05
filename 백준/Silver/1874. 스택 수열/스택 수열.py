N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

stack = [1]
rst = ['+']
num, idx = 1, 0
while idx < N:
    if num < arr[idx]:
        while num != arr[idx]:
            num += 1
            stack.append(num)
            rst.append('+')

        stack.pop()
        rst.append('-')
    else:
        var = stack.pop()
        if var != arr[idx]:
            rst = ['NO']
            break
        rst.append('-')
    idx += 1

for word in rst:
    print(word)
