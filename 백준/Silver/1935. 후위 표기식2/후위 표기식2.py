number = int(input())
expression = list(input())
four_opr = '+-*/'
lst = []
stack = []

for _ in range(number):
    lst.append(int(input()))

dic = dict(zip(list(map(chr, range(65, 91))), [0] * 26))

for word in expression:
    if word in four_opr:
        if word == '+':
            stack.append(stack.pop() + stack.pop())
        elif word == '*':
            stack.append(stack.pop() * stack.pop())
        elif word == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)
    else:
        if not dic[word]:
            dic[word] = lst.pop(0)
        stack.append(dic[word])

print(f'{stack[0]:.2f}')