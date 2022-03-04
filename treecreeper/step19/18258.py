import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

queue = deque([])

def push(n):
    queue.append(n)

def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.popleft())

def size():
    print(len(queue))

def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])


for i in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        push(int(cmd[1]))

    if cmd[0] == 'pop':
        pop()

    if cmd[0] == 'size':
        size()

    if cmd[0] == 'empty':
        empty()

    if cmd[0] == 'front':
        front()

    if cmd[0] == 'back':
        back()