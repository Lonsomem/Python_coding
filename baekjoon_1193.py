N = int(input())
n = 0
if N != 1:
    while n*(n+1) / 2 < N:
        n += 1
    space = n*(n+1) / 2 - N
    if n%2 == 0:
        print("%d/%d"%(n - space, space + 1))
    else:
        print("%d/%d"%(space + 1, n - space))
else:
    print("1/1")