while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if a == b or b == c or a == c:
        print("wrong")
    if a > b:
        if a > c:
            l = a
        else:
            l = c
    else:
        if b > c:
            l = b
        else:
            l = c
    if l*l == a*a + b*b:
        print("right")
    else:
        print("wrong")