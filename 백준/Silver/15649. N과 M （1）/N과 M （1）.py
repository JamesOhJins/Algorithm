N, M = map(int, input().split())
nums = []

def dfs():
    if len(nums) == M:
        print(' '.join(map(str,nums)))
        return
    else:
        for i in range(1,N+1): 
            if i not in nums:
                nums.append(i) 
                dfs()
                nums.pop()
dfs()