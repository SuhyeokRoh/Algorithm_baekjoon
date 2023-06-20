lst = []
for _ in range(4):
    lst.append(int(input()))
    
if lst[0] == 8 or lst[0] == 9:
    if lst[1] == lst[2]:
        if lst[3] == 8 or lst[3] == 9:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")