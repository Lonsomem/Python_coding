N = int(input())
n = 0
t = 0
if N % 5 != 0:
    while N % 5 != 0:
        n += 1
        N = N - 3
        if N == 0:
            print(n)
        elif N < 0:
            print(-1)
            break
    if N >= 5:
        while N != 0:
            t += 1
            N = N - 5
        if N == 0:
            print(n+t)
else:
    while N != 0:
        n += 1
        N = N - 5
    print(n)