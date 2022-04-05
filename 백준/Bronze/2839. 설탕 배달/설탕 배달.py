N = int(input())

count = 0
failed = False
while N > 0:
    if N%5 == 0:
        N -= 5
        count += 1
    elif N %3 == 0:
        N -= 3
        count += 1
    elif N > 5:
        N -= 5
        count +=1 
    else:
        print(-1)
        failed = True
        break

if count != 0 and failed == False:
    print(count)
        