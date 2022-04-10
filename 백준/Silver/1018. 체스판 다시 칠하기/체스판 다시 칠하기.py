h,w = map(int,input().split())
board = []
for i in range (h):
    board.append(str(input()))
current_min = h*w

def find_diff(start_x, start_y):
    white = False
    diff = 0
    for i in range (start_y,8+start_y):
        if white:
            white = False
        elif not white:
            white = True
        for j in range(start_x,8+start_x):
            if board[i][j] == "B" and white:
                diff += 1
            elif board[i][j] == "W" and not white:
                diff += 1
            if white:
                white = False
            elif not white:
                white = True
    if diff < current_min:
        return diff
    else:
        return current_min

def find_diff_b(start_x, start_y):
    white = False
    diff = 0
    for i in range (start_y,8+start_y):
        if white:
            white = False
        elif not white:
            white = True
        for j in range(start_x,8+start_x):
            if board[i][j] == "W" and white: 
                diff += 1
            elif board[i][j] == "B" and not white:
                diff += 1
            if white:
                white = False
            elif not white:
                white = True
    if diff < current_min:
        return diff
    else:
        return current_min

if h == 8 and w == 8:
    current_min = find_diff(0,0)
    current_min = find_diff_b(0,0)
elif h == 8 and w>8:
    for i in range(w-7):
        current_min = find_diff(i,0)
        current_min = find_diff_b(i,0)
elif w == 8 and h>8:
    for i in range(h-7):
        current_min = find_diff(0,i)
        current_min = find_diff_b(0,i)
else:
    for i in range(w-7):
        for j in range(h-7):
            current_min =find_diff(i,j)
            current_min = find_diff_b(i,j)
print(current_min)
