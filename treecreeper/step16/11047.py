n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
cnt = 0

for coin in coins:
    temp = k//coin
    if temp > 0:
        cnt += temp
        k -= temp*coin

print(cnt)