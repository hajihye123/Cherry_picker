n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
res = 0

res += distance[0] * cost[0]
min_cost = cost[0]

for i in range(1, n-1):
    if cost[i] > min_cost:
        res += distance[i] * min_cost
    else:
        res += distance[i] * cost[i]
        min_cost = cost[i]

print(res)