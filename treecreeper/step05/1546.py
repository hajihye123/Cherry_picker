n = int(input())
a = list(map(int, input().split()))
a.sort()

for i in range(n):
    a[i] = a[i] / a[n-1] * 100.0

sum = 0
for i in range(n):
    sum  += a[i]
print(sum/n)