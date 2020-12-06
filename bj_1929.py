import sys

M, N = map(int, sys.stdin.readline().split())

numlist = [0 for x in range(0, 1000001)]
numlist[0] = 0
numlist[1] = 0
for t in range(2, 1000001):
    for n in range(2, 1001):
        if n*n < t:
            if t % n == 0:
                break
            else:
                continue
        else:
            numlist[n] == 1

for i in range(M, N+1):
    if numlist[i] == 1:
        print(numlist[i])
    else:
        continue