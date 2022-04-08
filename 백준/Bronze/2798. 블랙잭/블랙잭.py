N, Target = map(int,input().split())
numbers = list(map(int,input().split()))
temp_ans = 0
found = False
diff = Target
for i in range (N - 2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = numbers[i] + numbers[j] + numbers[k]
            temp = Target - sum
            if(temp == 0):
                found = True
                break
            elif(temp < diff and sum < Target):
                diff = temp
                temp_ans = sum
if not found:
    print(temp_ans)
else:
    print(Target)