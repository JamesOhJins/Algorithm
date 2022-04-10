import sys

N = int(input())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))
nums.sort()
print(*nums,sep = "\n")