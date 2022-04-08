N = int(input())
digit = len(str(N))
min_num = N - digit*9 #각 자리수가 9로 체워졌을때 자릿수의 합이 N 이 될 가능성이 있는 최소 숫자
if min_num < 0:
    min_num = 0
def decomp():
    if digit == 1:
        if N % 2 == 0:
            return N//2
        else:
            return 0
    else:
        for i in range(min_num,N):
            temp = i
            for j in range(len(str(i))):
                add = str(i)[j]
                temp += int(add)
            if temp == N:
                return i
    return 0
print(decomp())