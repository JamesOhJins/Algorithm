import sys

N = int(input())
ans = []
for _ in range(N):
    nums = list(map(int, sys.stdin.readline().split()))
    temp = nums[0]
    nums[0] = nums[1]
    nums[1] = temp
    ans.append(nums)

ans.sort()

for i in range(len(ans)):
    print(ans[i][1], end=' ')
    print(ans[i][0])
    