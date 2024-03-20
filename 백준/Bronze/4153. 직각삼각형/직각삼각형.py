import sys

while True:
    a = list(map(int,sys.stdin.readline().split()))
    
    if a == [0,0,0]:
        break

    a.sort()
    
    if a[0]*a[0] + a[1]*a[1] == a[2]*a[2]:
        print('right')
    else:
        print('wrong')