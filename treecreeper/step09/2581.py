m = int(input())
n = int(input())
prime = []
for i in range(m, n + 1):
    cnt = 0
    if i == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:    # 자신을 나누는 숫자가 자신뿐일 때
        prime.append(i)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))