import sys 

n = int(input())
num = [0 for _ in range(0,n)]

for i in range(0, n):
    num[i] = int(sys.stdin.readline())

num.sort()

for j in num:
    print(j)