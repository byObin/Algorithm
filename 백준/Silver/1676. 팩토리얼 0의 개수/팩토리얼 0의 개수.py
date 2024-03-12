import sys

n = int(sys.stdin.readline())

fac = 1
for i in range(1,n+1):
    fac *= i

cnt = 0
for j in str(fac)[::-1]:
    if j != '0':
        print(cnt)
        break
    else:
        cnt += 1