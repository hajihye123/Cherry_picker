'''
1: 1개
2: 2~7 해서 6개
3: 8~19해서 12개
4: 20~37 해서 18개
'''
n = int(input())
num = 1
i = 1
cnt = 1
while True:
    if n == 1:
        break
    else:
        temp = num
        num += 6*i
        cnt += 1
        if temp < n <= num:
            break
        i+=1

print(cnt)