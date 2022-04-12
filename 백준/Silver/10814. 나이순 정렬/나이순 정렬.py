import sys

N = int(input())
names = []

for _ in range(N):
    a,b = sys.stdin.readline().split()
    name = [int(a),str(b)]
    names.append(name)
names.sort(key=lambda names: names[0])
for i in range(N):
    print(names[i][0], end=" ")
    print(names[i][1])
