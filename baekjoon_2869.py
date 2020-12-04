A, B, V = map(int, input().split())

duration = (V-B) / (A-B)

if duration == int(duration):
    print(int(duration))
else :
    print(int(duration)+1)