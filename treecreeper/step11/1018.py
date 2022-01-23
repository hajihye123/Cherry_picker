n, m = map(int, input().split())
original = []
count = []

for _ in range(n):
    original.append(input())

for i in range(n-7):
    for j in range(m-7):
        first_W = 0
        first_B = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if original[k][l] == 'W':
                        first_W += 1
                    if original[k][l] == 'B':
                        first_B += 1
                else:
                    if original[k][l] == 'B':
                        first_W += 1
                    if original[k][l] == 'W':
                        first_B += 1
        count.append(min(first_W, first_B))

print(min(count))