n = int(input())    # 26
cycle = 0
new = n
while True:
    a = new // 10     # 2
    b = new % 10      # 6
    sum = (a + b) % 10     # 8
    new = b * 10 + sum
    cycle += 1
    if new == n:
        print(cycle)
        break