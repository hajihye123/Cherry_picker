n = input()
nums = []

for i in n:
    nums.append(i)

nums.sort(reverse=True)
res=''

for i in range(len(n)):
    res += nums[i]

print(res)