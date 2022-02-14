n, k = map(int, input().split())
items = [[0,0]]

for i in range(n):
    w, v = map(int, input().split())
    items.append([w, v])

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):         # i번째 물건
    for j in range(1, k+1):     # j: 수용 가능한 최대 무게
        weight = items[i][0]
        value = items[i][1]

        if weight > j:     # 해당 물건을 넣을 수 없는 경우
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n][k])