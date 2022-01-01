t = int(input())
p = ''
for i in range(t):
    r, s = input().split()
    for j in s:
        p += int(r)*j
    print(p)
    p = ''