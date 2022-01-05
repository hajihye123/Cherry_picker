'''
각 줄마다 숫자가 1개, 2개, 3개 , ... , n개씩 증가하므로
x에서 1, 2, 3, ... , n을 빼면서 몇 번째 줄인지 알아낸 후,
홀수 줄인지, 짝수 줄인지에 따라 분모와 분자를 결정한다.
'''

x = int(input())
line = 1
a = 0
b = 0
while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    a = x
    b = line - x + 1
else:
    a = line - x + 1
    b = x

print('%d/%d'%(a, b))