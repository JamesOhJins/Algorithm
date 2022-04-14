N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()
sum = 0
for i in range(N):
    sum += (a[i] * b[N-1-i])
print(sum)