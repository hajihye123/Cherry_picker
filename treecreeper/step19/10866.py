import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
deq = deque([])

def push_front(n):
    deq.appendleft(n)

def push_back(n):
    deq.append(n)

def pop_front():
    if len(deq) == 0:
        print(-1)
    else:
        print(deq.popleft())

def pop_back():
    if len(deq) == 0:
        print(-1)
    else:
        print(deq.pop())

def size():
    print(len(deq))

def empty():
    if len(deq) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(deq) == 0:
        print(-1)
    else:
        print(deq[0])

def back():
    if len(deq) == 0:
        print(-1)
    else:
        print(deq[-1])

for i in range(n):
    cmd = input().split()

    if cmd[0] == 'push_front':
        push_front(cmd[1])
    if cmd[0] == 'push_back':
        push_back(cmd[1])
    if cmd[0] == 'pop_front':
        pop_front()
    if cmd[0] == 'pop_back':
        pop_back()
    if cmd[0] == 'size':
        size()
    if cmd[0] == 'empty':
        empty()
    if cmd[0] == 'front':
        front()
    if cmd[0] == 'back':
        back()