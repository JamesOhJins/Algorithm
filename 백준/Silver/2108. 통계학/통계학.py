from statistics import multimode 
import sys
N = int(input())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))
mode_num = multimode(nums)
mode_num.sort()
nums.sort()
print(round(sum(nums)/N))
print(nums[N//2])
if len(mode_num) > 1:
    print(mode_num[1])
else:
    print(mode_num[0])
print(max(nums)-min(nums))
