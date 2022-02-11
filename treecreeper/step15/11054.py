import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

dp_decrease = [0] * n

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if nums[i] > nums[j] and dp_decrease[i] < dp_decrease[j]:
            dp_decrease[i] = dp_decrease[j]
    dp_decrease[i] += 1

res = [0] * n

for i in range(n):
    res[i] = dp[i] + dp_decrease[i] - 1

print(max(res))