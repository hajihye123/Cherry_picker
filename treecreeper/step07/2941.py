s = input()
alp = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=', 'dz=']
cnt = len(s)
for i in range (len(alp)-1):
    cnt -= s.count(alp[i])
cnt -= s.count(alp[len(alp)-1])
print(cnt)