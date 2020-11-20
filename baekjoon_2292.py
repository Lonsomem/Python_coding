N = int(input())
n = 2
if N > 8:
    while N - (3*(n+1)*(n+1)-9*(n+1)+8) >= 0:
        n += 1
    print(n)
else:
    if N == 1:
        print(1)
    else:
        print(2)