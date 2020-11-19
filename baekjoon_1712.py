A, B, C = map(int,input().split())

if (C-B) != 0:
    if (A / (C-B)) > 0:
        n = int(A / (C-B)) + 1
        print(n)
    else:
        print(-1)
else:
    print(-1)
