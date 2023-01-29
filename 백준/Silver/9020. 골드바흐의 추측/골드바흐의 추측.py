import sys

loop = int(sys.stdin.readline())

lst = [1] * 10000
# 에라토스테네스의 체를 활용하여 10000까지 범위의 소수를 구한다. 
for i in range(2,101):
# 범위는 2부터 끝값인 10000의 루트값, 100까지만 계산하면 되므로 101로 설정한다.
    if lst[i] == 1:
# 모든 리스트를 1로 설정하고, 
# i가 소수에 해당하면 1이므로 이때 i+i부터 i씩 증가한 인덱스는 전부 0으로 바꾼다.
        for j in range(i+i,10000,i):
            lst[j] = 0
# 전부 돌린 후, lst에서 1을 갖는 인덱스 값들만 꺼내온다.
rst = [i for i in range(2,10000) if lst[i] == 1]

for _ in range(loop):
    num = int(sys.stdin.readline())
    set_lst = set([n for n in rst if n < num])
    i, compare_num = 0, num

    while rst[i] <= (num - rst[i]):
        gold = num - rst[i]
        if gold in set_lst and (gold - rst[i]) < compare_num:
            val = (rst[i], gold)
            compare_num = gold - rst[i]
        i += 1
    print(val[0], val[-1])