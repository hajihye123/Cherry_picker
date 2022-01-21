def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):   # 소수 판별은 판별하고자 하는 숫자의 제곱근까지만 검사하면 된다.
            if num % i == 0:
                return False
        return True

m, n = map(int, input().split())

for i in range(m, n + 1):
    if isPrime(i):
        print(i)