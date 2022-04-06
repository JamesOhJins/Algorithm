M,N = map(int,input().split())


def prime_list(n):
    prime = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if prime[i] == True:           
            for j in range(i+i, n, i): 
                prime[j] = False
    for i in range(2, n):
        if prime[i] == True and i >= M:
            print(i)
            
prime_list(N+1)
