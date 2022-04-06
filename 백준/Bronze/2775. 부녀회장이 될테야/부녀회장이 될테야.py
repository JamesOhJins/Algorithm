from array import *
N = int(input())
for _ in range(N):
    floors = int(input())
    number = int(input())
    people = []
    base = []
    for i in range(1, number + 1):
        base.append(i)
    people.insert(0,base)
    for i in range(1, floors +1):
        temp = []
        for j in range(1, number + 1):
            if j == 1:
                temp.append(1)
                people.insert(i,temp)
            else:# 102호
                num = people[i-1][j-1] + people[i][j-2]
                temp.append(num)
                people[i] = temp
    print(people[floors][number-1])