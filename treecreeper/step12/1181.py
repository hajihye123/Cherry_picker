import sys

n = int(sys.stdin.readline())
words = []
for i in range(n):
    word = sys.stdin.readline()
    if word not in words:
        words.append(word)

words.sort()
words.sort(key=len)

for i in range(len(words)):
    print(words[i], end='')