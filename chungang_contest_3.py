l = int(input())
schedule_list = []
slicing_list = []
for n in range(l):
    x, y = map(int, input().split())
    one_schedule = [x for x in range(x, y+1)]
    for t in one_schedule:
        schedule_list.append(t)

t = schedule_list.sort()

s = list(set(schedule_list))
for n in range(len(s)-1):
    if s[n+1] != (s[n] + 1):
        slicing_list.append(n)

for n in slicing_list:
    end_index =  