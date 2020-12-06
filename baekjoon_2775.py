C = int(input())

def plus():  
    global b 
    global a
    global k
    global n
    for x in range(k):
        for i in range(0, n):
            for x in range(0, i+1):
                b[i] += a[x] 
        a = b
        b = [0 for i in range(n)]

for n in range(C):
    k = int(input())
    n = int(input())
    a = list(range(1, n+1))
    b = [0 for i in range(n)]
    plus()
    print(a[n-1])
    


