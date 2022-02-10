import sys

input = sys.stdin.readline
n = int(input())
score = [0] * 300
for i in range(n):
    score[i] = int(input())

res = [0] * 300

res[0] = score[0]
res[1] = score[0] + score[1]
res[2] = max(score[1] + score[2], score[0] + score[2])

for i in range(3, n):
    res[i] = max(res[i-3] + score[i-1] + score[i], res[i-2] + score[i])    # 마지막 계단 전(i-1)을 밟은 경우 vs 밟지 않은 경우

print(res[n-1])