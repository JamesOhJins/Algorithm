import sys
N = int(input())

nums = list(map(int, sys.stdin.readline().split()))
sorted_list = sorted(nums)
sorted_dic = {}
for i in sorted_list:
    if i not in sorted_dic:
        sorted_dic[i] = len(sorted_dic)
cnt = 1
for j in nums:
    if cnt < N:
        print(sorted_dic[j], end=" ")
        cnt += 1
    else:
        print(sorted_dic[j])