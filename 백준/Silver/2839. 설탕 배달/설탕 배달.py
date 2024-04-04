n = int(input())

for i in range(n//5,-1,-1):
    if (n-(i*5))%3 == 0:
        print(i + (n-(i*5))//3)
        break
else:
    print(-1)