import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

queue = deque(range(1, n+1))
res = []

print('<', end='')

while len(queue) != 0:
    for i in range(k):
        queue.append(queue.popleft())
    num = queue.pop()
    print(num, end='')
    res.append(num)

    if len(queue) == 0:
        continue
    else:
        print(', ', end='')
print('>')