all = set(range(1, 10001))
num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    num.add(i)

self_num = sorted(all - num)
for i in self_num:
    print(i)