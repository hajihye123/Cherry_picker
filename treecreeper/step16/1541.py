n = input()
formula = n.split('-')
res = 0

for i in formula[0].split('+'):
    res += int(i)

for i in formula[1:]:
    for j in i.split('+'):
        res -= int(j)

print(res)