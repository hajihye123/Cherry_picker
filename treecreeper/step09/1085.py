x, y, w, h = map(int, input().split())

# (0, h)            (w, h)
#
#          (x, y)
#
# (0, 0)            (w, 0)

print(min(x, y, (h-y), (w-x)))