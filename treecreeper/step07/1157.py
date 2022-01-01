s = input()
ans = [0]*26
all = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s = s.lower()

for i in s:
    if i in all:
        ans[all.index(i)] += 1

maxnum = max(ans)
cnt = ans.count(maxnum)
if cnt == 1:
    print(all[(ans.index(max(ans)))].upper())
else:
    print('?')