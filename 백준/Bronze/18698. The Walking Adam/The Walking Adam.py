for _ in range(int(input())):
    word = input()
    rst = 0
    for x in word:
        if x == "D":
            break
        else:
            rst += 1
    print(rst)