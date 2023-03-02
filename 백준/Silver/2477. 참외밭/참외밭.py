K = int(input())
diff = [[0,0] for _ in range(6)]
width = height = 0
for i in range(6):
    direction, length = map(int, input().split())
    diff[i] = [direction, length]

for idx in range(6):
    if [diff[idx%6][0], diff[(idx+1)%6][0]] == [diff[(idx+2)%6][0], diff[(idx+3)%6][0]]:
        vsb_area = diff[(idx+1)%6][1] * diff[(idx+2)%6][1]
    if diff[idx][0] == 1 or diff[idx][0] == 2:
        if width < diff[idx][1]:
            width = diff[idx][1]
    if diff[idx][0] == 3 or diff[idx][0] == 4:
        if height < diff[idx][1]:
            height = diff[idx][1]

print((width * height - vsb_area) * K)