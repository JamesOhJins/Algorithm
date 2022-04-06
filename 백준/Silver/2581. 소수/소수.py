M = int(input())
N = int(input())
ans = 0
prime_numbers = []
first = True
first_num = 0

for i in range(M,N+1):
    cnt = 0
    for j in range(2,i):
        if i % j == 0:
            cnt += 1
    if cnt == 0:
        prime_numbers.append(i)
if 1 in prime_numbers:
    prime_numbers.remove(1)

if sum(prime_numbers) == 0:
    print(-1)

else: 
    print(sum(prime_numbers))
    print(min(prime_numbers))