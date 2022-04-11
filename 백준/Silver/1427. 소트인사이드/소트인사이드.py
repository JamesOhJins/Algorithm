N = str(input())
nums = []
for i in N:
    nums.append(i)
nums.sort(reverse = True)
print(*nums, sep = '')