n = int(input())
cnt = 0
for i in range(1, n+1):
    if i <= 99:
        cnt += 1
    else:
        if i == 1000:
            continue
        elif (i%10 - (i//10)%10) == ((i//10)%10 - (i//100)%10):
            cnt += 1
print(cnt)