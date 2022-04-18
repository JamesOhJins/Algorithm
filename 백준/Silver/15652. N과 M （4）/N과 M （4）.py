N, M = map(int, input().split())
nums = []

def dfs():
    if len(nums) == M:
        sorted_list = sorted(nums)
        if nums == sorted_list:
            print(' '.join(map(str,nums)))
        
        return
    else:
        for i in range(1,N+1):
            nums.append(i)
            dfs()
            nums.pop()
dfs()