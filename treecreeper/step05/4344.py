n = int(input())
a = []
cnt = 0
res = 0
for i in range(n):
    a = list(map(int, input().split()))
    avg = sum(a[1:])/ a[0]
    for j in range(1, a[0]+1):
        if a[j] > avg:
            cnt += 1
    res = cnt / (len(a)-1) * 100.0
    print("{:.3f}%".format(res))
    cnt = 0
    res = 0
    a = []