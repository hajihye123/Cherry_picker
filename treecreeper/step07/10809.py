s = input()
ans = [-1] * 26
all = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alp = []
cnt = 0
for i in s:
    if i not in alp:
        ans[all.index(i)] = cnt
        alp.append(i)
    cnt += 1
for i in range(26):
    print(ans[i], end=' ')

############################# 간단한 방법

'''
S = input()

a = 'abcdefghijklmnopqrstuvwxyz'

for i in a:
    print(str(S.find(i)), end = ' ')
'''