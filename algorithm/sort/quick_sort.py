# 퀵정렬

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

def quick_sort(nums, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while (left <= right):
        # 왼쪽에서는 피벗보다 작은 값을 찾는다
        while (left <= end and nums[left] <= nums[pivot]):
            left += 1
        # 오른쪽에서는 피벗보다 큰 값을 찾는다
        while (right > start and nums[right] >= nums[pivot]):
            right -= 1
        # 엇갈렸다면(피벗 값 - right(큰 값) - left(작은 값)) 작은 값과 피벗 교체
        if (left > right):
            nums[right], nums[pivot] = nums[pivot], nums[right]
        # 엇갈리지 않았다면(피벗 값 - left(작은 값) - right(큰 값)) 작은 값과 큰 값 교체
        else:
            nums[left], nums[right] = nums[right], nums[left]
        quick_sort(nums, start, right-1)
        quick_sort(nums, right+1, end)

quick_sort(nums, 0, len(nums)-1)

for i in range(n):
    print(nums[i])