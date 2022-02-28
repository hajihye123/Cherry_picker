t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    idx = max(a, b)
    gcd = 0
    lcm = 0

    for i in range(1, idx + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    lcm = gcd * (a // gcd) * (b // gcd)
    print(lcm)