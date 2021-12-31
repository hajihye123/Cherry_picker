nums = []
for i in range(10):
    nums.append((int(input())) % 42)
res = []
for num in nums:
    if num not in res:
        res.append(num)
print(len(res))