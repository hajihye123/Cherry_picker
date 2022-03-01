import sys

def push(n):
    stack.append(n)

def pop():
    if len(stack) != 0:
        print(stack[-1])
        stack.pop()
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) != 0:
        print(stack[-1])
    else:
        print(-1)


input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    cmd = list(map(str, input().split()))

    if cmd[0] == 'push':
        push(int(cmd[1]))
    if cmd[0] == 'pop':
        pop()
    if cmd[0] == 'size':
        size()
    if cmd[0] == 'empty':
        empty()
    if cmd[0] == 'top':
        top()