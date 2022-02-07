import sys

input = sys.stdin.readline
n = int(input())
nums = []

for i in range(n):
    nums.append(list(map(int, input().split())))

k = 2
for i in range(1, len(nums)):
    for j in range(k):
        if j == 0:
            nums[i][j] = nums[i][j] + nums[i-1][j]
        elif i == j:
            nums[i][j] = nums[i][j] + nums[i-1][j-1]
        else:
            nums[i][j] = max(nums[i-1][j-1], nums[i-1][j]) + nums[i][j]
    k += 1
print(max(nums[n-1]))