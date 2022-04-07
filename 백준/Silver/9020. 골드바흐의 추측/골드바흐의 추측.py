T = int(input())
prime_numbers = []
def prime_nums(n):
    prime = [True] * n
    m = int(n**0.5)
    for i in range(2,m + 1):
        if prime[i] == True:
            for j in range(i+i,n,i):
                prime[j] = False
    for i in range(2,n):
        if prime[i] == True:
            prime_numbers.append(i)

def add(n):
    temp = n//2
    if temp in prime_numbers:
        print(temp,temp)
    else:
        for i in range(temp,0,-1):
            if (i in prime_numbers) and ((n - i) in prime_numbers):
                print(i, n - i)
                break

prime_nums(10001)

for i in range(T):
    N = int(input())
    add(N)