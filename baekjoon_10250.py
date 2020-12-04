C = int(input())

for n in range(C):
    H, W, N = map(int, input().split())
    F = N % H
    R = N // H + 1
    if F != 0:
        if R > 9:
            print(F, end='')
            print(R)
        else:
            print(F, end='')
            print(0, end='')
            print(R)
    else:
        if R > 10:
            print(H, end='')
            print(R-1)
        else:
            print(H, end='')
            print(0, end='')
            print(R-1)
