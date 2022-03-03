import sys

#input = sys.stdin.readline

n = int(input())
stack = []
res = []
cnt = 0
state = True

for i in range(n):
    num = int(input())

    while cnt < num:
        cnt += 1
        stack.append(cnt)
        res.append('+')

    if stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        state = False
        break

if state == True:
    for i in res:
        print(i)
else:
    print('NO')