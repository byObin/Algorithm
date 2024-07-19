t = int(input())

for _ in range(t):
    n = int(input())

    p = [0,1,1,1,2,2,3,4,5,7,9]

    if n <= 10:
        print(p[n])
    else:
        for i in range(11,n):
            p.append(p[i-1]+p[i-5])
        
        print(p[n-1]+p[n-5])
