num = list(map(int,input()))

num.sort(reverse=True)
n = list(map(str,num))
rst = ''.join(n)

print(rst)
