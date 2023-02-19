i = 0
while True:
    string = list(input())
    i += 1
    if '-' in string:
        break
    stack, cnt = [], 0

    for word in string:
        if word == '}':
            if not stack:
                cnt += 1
                stack.append('{')
            elif stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(word)
        else:
            stack.append(word)

    cnt += len(stack)//2

    print(f'{i}. {cnt}')
