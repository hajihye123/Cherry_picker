t = int(input())

for i in range (t):
    h, w, n = map(int, input().split())     # 층, 호수, 순서
    a = n // h + 1
    b = n % h
    if b == 0:
        b = h
        a -= 1
    print(b * 100 + a)