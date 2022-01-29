import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums2 = sorted(list(set(nums))) # 중복 제거 -> 각 숫자의 인덱스가 압축한 좌표

dic = {nums2[i]:i for i in range(len(nums2))}   # 숫자: 압축좌표 형태로 저장

for i in nums:
    print(dic[i], end=' ')