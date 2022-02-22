n = int(input())
times = []

for i in range(n):
    times.append(list(map(int, input().split())))

times.sort(key = lambda time: time[0])
times.sort(key = lambda time: time[1])

cnt = 0
start_time = 0
for time in times:
    if time[0] >= start_time:
        start_time = time[1]
        cnt += 1

print(cnt)