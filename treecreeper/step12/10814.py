import sys

n = int(sys.stdin.readline())
words = []

for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    words.append((int(a),b))

words.sort(key= lambda x:x[0])

for word in words:
    print(word[0], word[1], sep=' ', end='\n')