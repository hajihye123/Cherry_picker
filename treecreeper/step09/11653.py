n = int(input())
a = 2
nums = []
while True:
    if n == 1:
        break

    if n % a == 0:
        nums.append(a)
        n = n / a
        a = 2
    else:
        a += 1

for i in nums:
    print(i)