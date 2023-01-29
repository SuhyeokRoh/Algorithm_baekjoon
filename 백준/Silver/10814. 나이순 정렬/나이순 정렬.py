import sys

loop = int(sys.stdin.readline())
lst = [] 

for case in range(loop):
    age_name = sys.stdin.readline().split()
    age_name[0] = int(age_name[0])
    lst.append(age_name)

lst.sort(key=lambda x: x[0])

for x,y in lst:
    print(x,y)