for _ in range(int(input())):
    lst = list(map(int, input().split()))
    rst = 0
    for x in lst:
        if x >= 10:
            rst += 1
            
    print(*lst)
    
    if rst >= 3:
        print("triple-double")
    elif rst >= 2:
        print("double-double")
    elif rst >= 1:
        print("double")
    else:
        print("zilch")
    print()