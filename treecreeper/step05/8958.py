n = int(input())
a = []
for i in range(n):
    a.append(input())
res = 0
score = 1
for aa in a:
    for i in range(len(aa)):
        if aa[i] == 'O':
            res += score
            score += 1
        elif aa[i] == 'X':
            score = 1
    print(res)
    res = 0
    score = 1