var = str(input())
var = var.split()

match (int(var[0]) == 0, int(var[-1]) - 45 >= 0):
    case (True, True):
        print('{} {}'.format(var[0], int(var[-1]) - 45))
    case (True, False):
        minus_var = int(var[-1]) - 45
        print('23 {}'.format(60 + minus_var))
    case (False, True):
        print('{} {}'.format(var[0], int(var[-1]) - 45))
    case (False, False):
        minus_var = int(var[-1]) - 45
        print('{} {}'.format(int(var[0]) - 1, 60 + minus_var))