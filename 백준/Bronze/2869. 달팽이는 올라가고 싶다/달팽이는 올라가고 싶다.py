import math
A,B,V = map(int,input().split())
V = V - A
X = math.ceil((V/(A-B)) + 1)

print(X)