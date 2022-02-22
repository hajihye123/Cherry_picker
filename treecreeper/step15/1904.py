import sys

input = sys.stdin.readline
n = int(input())
dp = [0] * 1000001
dp[1] = 1   # 이진수 1
dp[2] = 2   # 이진수 00, 11

for i in range(3, n + 1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])