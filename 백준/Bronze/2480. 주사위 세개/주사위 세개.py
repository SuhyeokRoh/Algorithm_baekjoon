dice = str(input())
dice = list(map(int,dice.split()))

match (dice[0]-dice[1], dice[1]-dice[-1]):
    case (0,0):
        print(10000 + dice[0] * 1000)
    case (0,_):
        print(1000 + dice[0] * 100)
    case (_,0):
        print(1000 + dice[1] * 100)
    case (_,_):
        if dice[0] == dice[-1]:
            print(1000 + dice[0] * 100)
        else:
            var = max(dice)
            print(var * 100)
        
        
        