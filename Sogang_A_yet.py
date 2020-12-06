C = int(input())
Fext = {}
Flist = []
for n in range(C):
    F = input()
    F = F.split('.')
    Flist.append(F[1])
Flist_Set = sorted(Flist)
for n in range(len(Flist)):
    
    if n == F:
        Fext[n] += 1
    else:
        Fext[F] = 1

Fext = sorted(Fext.items())
print(Fext)
for n in Fext:
    print(n[0], " ", n[1])

