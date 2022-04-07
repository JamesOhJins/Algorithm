N = int(input())
def hanoi(N, start, via, to):
    if N == 1:
        print(start, to)
    else:
        hanoi(N-1, start, to, via)
        print(start, to)
        hanoi(N-1, via, start, to)
print((2**N) -1)
hanoi(N,'1','2','3')