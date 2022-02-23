n = int(input())
p = list(map(int, input().split()))

p.sort()
res = 0

for i in range(n):
    res += p[i] * (n-i)

print(res)