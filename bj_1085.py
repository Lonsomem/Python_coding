x, y, w, h = map(int,input().split())
nl = [x, y, w-x, h-y]
minnum = nl[0]
for n in range(len(nl)):
    if minnum > nl[n]:
        minnum = nl[n]

print(minnum)