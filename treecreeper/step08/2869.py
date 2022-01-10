import math

a, b, v = map(int, input().split())
res = (v-b)/(a-b)
print(math.ceil(res))