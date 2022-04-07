T = int(input())
for i in range (T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    r3 = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    range = [float(r1),float(r2),r3]
    max_num = max(range)
    range.remove(max_num)

    if r3 == 0 and r1 == r2:
        print(-1)
    elif r3 == 0:
        print(0)
    elif max_num == sum(range):
        print(1)
    elif max_num > sum(range):
        print(0)
    else:
        print(2)