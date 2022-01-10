n = int(input())
nums = list(map(int, input().split()))
res = 0

for i in range(n):
    cnt = 0
    if nums[i] == 1:
        continue
    for j in range(2, nums[i] + 1):
        if nums[i] % j == 0:
            cnt += 1
    if cnt == 1:    # 자신을 나누는 숫자가 자신뿐일 때
        res += 1
print(res)