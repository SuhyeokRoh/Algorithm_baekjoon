num = str(input())

num_list = list(num.split())
diff_list = [1,1,2,2,2,8]
need_chess = []

for n in range(len(num_list)):
    if int(num_list[n]) == diff_list[n]:
        need_chess.append(0)
    else:
        need_chess.append(diff_list[n] - int(num_list[n]))
for i in range(len(need_chess)):
    print(need_chess[i],end=' ')