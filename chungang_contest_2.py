a, b, c = map(int, input().split())
x1, x2, y1, y2 = map(int, input().split())
if b != 0:
    if ((-(a/b)*x1 -(c/b)) <= y1 and (-(a/b)*x2 -(c/b)) <= y1) or ((-(a/b)*x1 -(c/b)) >= y2 and (-(a/b)*x2 -(c/b)) >= y2):
        print("Lucky")
    else:
        print("Poor")
else :
    if (-(c/a) < x1) or (-(c/a) > x2):
        print("Lucky")
    else:
        print("Poor")