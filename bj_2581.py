import math

start_num = int(input())
end_num = int(input())

answer = 0
primelist = []

numlist = [n for n in range(start_num, end_num+1)]

for i in range(len(numlist)):
    t = 2
    if numlist[i] != 1:
        while numlist[i] % t != 0:
            t += 1    
        if t == numlist[i]:
            answer += numlist[i]
            primelist.append(numlist[i])
        else:
            continue
    else:
        continue

if answer != 0:
    print(answer)
    print(primelist[0])
else:
    print(-1)