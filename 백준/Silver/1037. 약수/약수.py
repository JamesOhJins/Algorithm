N = int(input())
nums = list(map(int, input().split()))
if len(nums) == 1:
    print(nums[0] ** 2)
else:
    print(max(nums) * min(nums))