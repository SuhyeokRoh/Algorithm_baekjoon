import sys

n_num = int(sys.stdin.readline())

n_list = set(map(int,sys.stdin.readline().split()))

m_num = int(sys.stdin.readline())

m_list = list(map(int,sys.stdin.readline().split()))

for number in m_list:
    if number in n_list:
        print(1)
    else:
        print(0)