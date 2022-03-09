import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

res = [0, 0]

def dp(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                dp(x, y, n//2)
                dp(x, y+n//2, n//2)
                dp(x+n//2, y, n//2)
                dp(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        res[0] += 1
    else:
        res[1] += 1

dp(0, 0, n)
print(res[0], res[1], sep='\n')