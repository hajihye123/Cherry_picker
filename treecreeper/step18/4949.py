import sys

#input = sys.stdin.readline

while True:
    vps = input()
    stack = []

    if vps == '.':
        break

    for j in vps:
        if j in ('(', '['):
            stack.append(j)
        elif j == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(j)
                break
        elif j == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(j)
                break

    if len(stack) == 0:
        print('yes')
    else:
        print('no')