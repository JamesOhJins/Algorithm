def checkMultiple(a,b):
    if a > b:
        if a % b == 0:
            return "multiple"
        else:
            return "neither"
    elif b > a:
        if b % a == 0:
            return "factor"
        else:
            return "neither"    
x,y = map(int,input().split())
while not x == 0 and not y == 0:
    print(checkMultiple(x,y))
    x,y = map(int,input().split())