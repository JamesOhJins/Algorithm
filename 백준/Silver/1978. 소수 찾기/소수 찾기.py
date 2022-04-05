N = int(input())
numbers = list(input().split())
count = 0
prime_numbers = list(range(2,1000))

for i in range(1,1000):
    for j in range(2,i):
        if i % j == 0 and i in prime_numbers:
            prime_numbers.remove(i)
for i in numbers:
    if int(i) in prime_numbers:
        count += 1
print(count)
