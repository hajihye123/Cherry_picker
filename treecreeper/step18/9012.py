import sys

input = sys.stdin.readline
t = int(input())

for i in range(t):
    vps = input()
    stack = []

    for j in vps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(j)
                break
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')