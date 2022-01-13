# 선택정렬

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if nums[min_index] > nums[j]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]

for i in range(n):
    print(nums[i])