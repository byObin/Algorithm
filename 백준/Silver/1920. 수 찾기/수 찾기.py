import sys

def bin_search(list, key):

    high = 0
    low = len(list) - 1 

    while True:
        mid = (high + low) // 2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            high = mid + 1
        else:
            low = mid - 1
        
        if high > low:
            break
    
    return -1


n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
test = list(map(int, sys.stdin.readline().split()))

a.sort()

for i in test:
    result = bin_search(a,i)
    if result == -1:
        print('0')
    else:
        print('1')