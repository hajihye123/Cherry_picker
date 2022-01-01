n = int(input())
nums = int(input())
sum = 0
for i in range(n):
    sum += (nums%10)
    nums = nums//10
print(sum)