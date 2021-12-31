import copy
nums = []
for i in range(9):
    nums.append(int(input()))

nums_copy = copy.deepcopy(nums)
nums.sort()
max = nums[8]

for i in range(9):
    if nums_copy[i] == max:
        print(max)
        print(i+1)
        break