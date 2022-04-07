x,y,w,h = map(int,input().split())

distances = []
distances.append(w-x)
distances.append(h-y)
distances.append(x)
distances.append(y)
print(min(distances))