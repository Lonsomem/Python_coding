import math

C = int(input())

num_list = list(map(int, input().split()))

answer = 0

for n in range(C):
    i = 2
    if num_list[n] == 1:
        continue
    while num_list[n] % i != 0:
        i += 1

    
    if i == num_list[n]:
        answer += 1
    else:
        continue

print(answer)

        
        
