time = str(input())
p_t = int(input())

time = time.split()
H, M = int(time[0]), int(time[-1])

p_h, m = divmod(M+p_t,60)
h = (H + p_h) % 24
print('{} {}'.format(h,m))