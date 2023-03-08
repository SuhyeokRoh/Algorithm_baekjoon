import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dic = dict()

for _ in range(N):
    site, pwd = input().split()
    dic[site] = pwd

for _ in range(M):
    want_find = input().rstrip()
    print(dic[want_find])
