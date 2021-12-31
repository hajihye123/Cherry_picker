a = int(input())
b = int(input())
c = int(input())
res = a * b * c
cnt = [0] * 10

while res != 0:
    n = int(res % 10)
    cnt[n] += 1
    res = int(res / 10)
for i in range(10):
    print(cnt[i])