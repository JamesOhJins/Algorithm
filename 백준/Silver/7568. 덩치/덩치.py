N = int(input())
weight = []
height = []
rank = [1] * N
for i in range(N):
    w, h = map(int,input().split())
    weight.append(w)
    height.append(h)

for i in range(N-1):
    for j in range(i,N):
        if weight[i] > weight[j]:
            if height[i] > height[j]:
                rank[j] += 1
        elif weight[j] > weight[i]:
            if height[j] > height[i]:
                rank[i] += 1

print(*rank)