import sys

N = int(input())
ans = []
for _ in range(N):
    nums = list(map(int, sys.stdin.readline().split()))
    ans.append(nums)

ans.sort()

for i in range(len(ans)):
    print(ans[i][0], end=' ')
    print(ans[i][1])