N = int(input())
add = 6
count = 1
number = 1
while N > number:
    count += 1
    number += add
    add += 6
print(count)
