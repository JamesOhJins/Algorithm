import statistics
from statistics import mode
x = []
y = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
not_ans_x = mode(x)
not_ans_y = mode(y)
for i in range(2):
    x.remove(not_ans_x)
    y.remove(not_ans_y)
print(x[0],y[0])