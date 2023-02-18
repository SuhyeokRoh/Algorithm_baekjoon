word = list(input())
stack = []
cnt = 0

for spell in word:
    if spell == 'A':
        if stack and stack[-1] == 'P' and len(stack) > 1:
            stack.append(spell)
            cnt += 1
        else:
            break
    else:
        if not stack or stack[-1] == 'P':
            stack.append(spell)
            cnt += 1
        elif stack and stack[-1] == 'A':
            if len(stack) > 2:
                empty_str = spell
                for _ in range(3):
                    empty_str = stack.pop() + empty_str
                if empty_str == 'PPAP':
                    stack.append(spell)
                    cnt += 1
                else:
                    break
            else:
                break

if cnt == len(word) and len(stack) == 1:
    print('PPAP')
else:
    print('NP')

