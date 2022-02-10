import sys

input = sys.stdin.readline
n = int(input())

dp = [[0] * 10 for _ in range(n+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]   # 한자리 수인 경우 0~9까지 가능한 숫자의 수

mod = 1000000000

for i in range(2, n+1):
    # 계단 수가 0으로 끝나는 경우
    dp[i][0] = dp[i-1][1]
    # 계단 수가 9로 끝나는 경우
    dp[i][9] = dp[i-1][8]

    # 계단 수가 1~8로 끝나는 경우
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % mod)