M,N = map(int,input().split())
find_num = list(range(M,N+1))
diff_num = [1]
dble = 1
while N >= dble * dble:
    dble += 1

for i in range(2,dble+1):
    for j in range(2,int(N/i)+1):
        diff_num.append(i*j)
result = sorted(set(find_num) - set(diff_num))

for num in result:
    print(num)