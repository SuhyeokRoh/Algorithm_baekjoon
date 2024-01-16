import sys

name = {"ChongChong" : 0,}

for _ in range(int(input())):
    first, second = sys.stdin.readline().split()
    f_t, s_t = name.get(first), name.get(second)
    if (f_t == None) & (s_t == None):
        name[first], name[second] = 1, 1
    elif f_t == None:
        if name[second] == 0:
            name[first] = 0
        else:
            name[first] = 1
    elif s_t == None:
        if name[first] == 0:
            name[second] = 0
        else:
            name[second] = 1
    else:
        if name[first] == 0 or name[second] == 0:
            name[first], name[second] = 0, 0
print(len([k for k, v in name.items() if v == 0]))
