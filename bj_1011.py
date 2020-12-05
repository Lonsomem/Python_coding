C = int(input())

for n in range(C):
    start_n, end_n = map(int, input().split())
    i = 1
    while (i*i) < (end_n-start_n):
        i += 1
    x = i
    length = end_n - start_n
    if length == 1:
        print(1)
    elif length == 2:
        print(2)
    else:
        if (i*i) == length:
            print(i * 2 - 1)
        else:
            if length <= i:
                print(i * 2)
            else:
                while length > i:
                    length -= i
                    x += 1
                print(x)

