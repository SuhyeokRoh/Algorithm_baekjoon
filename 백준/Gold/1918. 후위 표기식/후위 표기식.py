math_exp = list(input())

four_operator = {'(' : 0, '+' : 1, '-' : 1, '*' : 2, '/' : 2}
posterior_notation = ''
stack = []

for spell in math_exp:
    if spell in four_operator.keys():
        if not stack or four_operator[stack[-1]] < four_operator[spell] or spell == '(':
            stack.append(spell)
        else:
            while stack and four_operator[stack[-1]] >= four_operator[spell]:
                posterior_notation += stack.pop()
            stack.append(spell)
    elif spell == ')':
        while stack[-1] != '(':
            posterior_notation += stack.pop()
        stack.pop()
    else:
        posterior_notation += spell
while stack:
    posterior_notation += stack.pop()

print(posterior_notation)