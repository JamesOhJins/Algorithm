import math
T = int(input())
for _ in range(T):
    H, W, N = map(int,input().split())
    floor = N % H
    if floor == 0:
        floor = H
    numb = math.ceil(N/H)
    if numb < 10:
        numb = '0' + str(numb)
    room_name = str(floor) + str(numb)
    print(room_name)