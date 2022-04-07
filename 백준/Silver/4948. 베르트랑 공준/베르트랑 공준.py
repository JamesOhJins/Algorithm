def prime(n):
    cnt = 0
    prime_numbers = [True] * (2*n+1)
    m = int((2*n+1)**0.5)
    for i in range(2,m+1):
        if prime_numbers[i] == True:
            for j in range(i+i, 2*n+1, i):
                prime_numbers[j] = False
    for i in range(n, 2*n+1):
        if prime_numbers[i] == True and i > n:
            cnt += 1
    print(cnt)
N = int(input())
while(N != 0):
    prime(N)
    N = int(input())