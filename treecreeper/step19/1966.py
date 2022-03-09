import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    critical = deque(map(int, input().split()))
    idx = deque([0] * a)
    idx[b] = 1   # 궁금한 값
    order = 0

    while True:
        if critical[0] == max(critical):
            order += 1
            if idx[0] == 1:
                print(order)
                break
            else:
                critical.popleft()
                idx.popleft()
        else:
            critical.append(critical.popleft())
            idx.append(idx.popleft())