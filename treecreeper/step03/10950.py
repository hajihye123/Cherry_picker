T = int(input())
arrayA = []
arrayB = []

for i in range (T):
    A, B = map(int, input().split())
    arrayA.append(A)
    arrayB.append(B)

for i in range (T):
    print(arrayA[i] + arrayB[i])