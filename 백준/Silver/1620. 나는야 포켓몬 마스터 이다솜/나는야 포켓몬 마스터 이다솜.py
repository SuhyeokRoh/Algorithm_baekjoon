import sys

loop1, loop2 = map(int,sys.stdin.readline().split())
dic = {}

for case in range(1,loop1+1):
    word = sys.stdin.readline().rstrip('\n')
    dic[case] = word
    dic[word] = case

for _ in range(loop2):
    f_w = sys.stdin.readline().rstrip('\n')
    if str.isdigit(f_w):
        print(dic.get(int(f_w)))
    else:
        print(dic.get(f_w))