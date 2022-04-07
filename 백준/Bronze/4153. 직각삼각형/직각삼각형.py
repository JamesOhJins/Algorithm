nums = list(map(int,input().split()))
while not 0 in nums:
    a = min(nums)
    nums.remove(a)
    c = max(nums)
    nums.remove(c)
    b = nums[0]
    nums.remove(b)

    if c**2 == a**2 + b**2:
        print("right")
    else:
        print("wrong")
    nums = list(map(int,input().split()))
