N = int(input())
words = []

for i in range(N):
    word = str(input())
    if word not in words:
        words.append(word)
words.sort()
words.sort(key = len)
print(*words, sep = "\n")