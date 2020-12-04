l, k = map(int, input().split())
final_list = []

for n in range(l):
    numlist = [int(x) for x in input().split()]
    final_list.append(numlist)

for n in range(len(final_list)):
    for s in range(k):
        for t in range(len(final_list[n])):    
            print("%d " %(final_list[n][t]) * k, end='')
        print("")