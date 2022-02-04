import sys

input = sys.stdin.readline
t = int(input())
# 1 2 3 4   5    6   7   8   9   10   11  12   13   14
# 1 1 1 2   2    3   4   5   7   9    12  16   21   28
#       1+1 1+1  1+2 1+3 1+4 2+5 2+7  3+9 4+12 5+16 7+21
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5
dp[9] = 7
dp[10] = 9


def pn(n):
    if dp[n] != 0:
        return dp[n]

    for i in range(10, n+1):
        dp[i] = dp[i-5] + dp[i-1]

    return dp[n]


for i in range(t):
    n = int(input())
    print(pn(n))