import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

max_res = -1e9
min_res = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global max_res, min_res

    if depth == n:
        max_res = max(total, max_res)
        min_res = min(total, min_res)
        return

    if plus:
        dfs(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)




dfs(1, nums[0], op[0], op[1], op[2], op[3])
print(max_res)
print(min_res)