import sys

a, b, c = map(int, sys.stdin.readline().split())
res = 0
if b >= c:
    res = -1
else:
    res = int(a/(c-b)+1)

print(res)