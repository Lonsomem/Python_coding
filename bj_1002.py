import math
C = int(input())

for q in range(C):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    if r1 > r2:
        lr = r1
        sr = r2
    else:
        lr = r2
        sr = r1
    
    if d == 0 and r1 == r2:
        print(-1)
    elif d > r1 + r2:
        print(0)
    elif d == r1 + r2:
        print(1)
    elif d < r1 + r2 and d + sr > lr:
        print(2)
    elif d + sr == lr:
        print(1)
    else:
        print(0)
    