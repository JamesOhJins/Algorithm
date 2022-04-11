import sys
N = int(input())
nums = []
appear = {}
for i in range(N):
    key = int(sys.stdin.readline())
    if key in appear:
        appear[key] +=1
    else:
        appear[key] = 1
sorted_keys = sorted(appear)
for i in sorted_keys:
    for j in range(appear[i]):
        print(i)