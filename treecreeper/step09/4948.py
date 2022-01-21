def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):   # 소수 판별은 판별하고자 하는 숫자의 제곱근까지만 검사하면 된다.
            if num % i == 0:
                return False
        return True

all_list = list(range(2, 246912))
prime = []

for i in all_list:
    if isPrime(i):
        prime.append(i)

n = int(input())

while True:
    num = 0
    if n == 0:
        break
    for i in prime:
        if n < i <= 2*n:
            num += 1
    print(num)
    num = 0
    n = int(input())