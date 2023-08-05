lst1 = list(map(int, input().split(" : ")))
lst2 = list(map(int, input().split(" : ")))

time, tmp = 0, 0

for i in range(2):
    if tmp:
        lst2[2-i] -= 1
        tmp = 0
    t = lst2[2-i] - lst1[2-i]
    if t < 0:
        tmp = 1
        t += 60
    time += t * (60 ** i)

if tmp:
    lst2[0] -= 1
hour = lst2[0] - lst1[0]
if hour < 0:
    hour += 24
time += hour * 3600

print(time)