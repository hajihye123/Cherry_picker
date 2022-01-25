import sys

n = int(sys.stdin.readline())
nums = []
count = [0] * 8001

for i in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)
    count[num+4000] += 1

nums.sort()

avg = sum(nums) / n
print(round(avg))
print(nums[n//2])

cnt = 0
max_count = max(count)
candidate = []

for i in range(8001):
    if count[i] == max_count:
        candidate.append(i - 4000)

candidate.sort()
if len(candidate) > 1:
    print(candidate[1])
else:
    print(candidate[0])

print(max(nums) - min(nums))