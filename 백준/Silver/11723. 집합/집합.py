import sys

input = sys.stdin.readline

m = int(input())
s = set()

for i in range(m):
    op = input().strip().split()
    if len(op) == 1:
        if op[0] == 'all':
            s = set([i for i in range(1,21)])
        else:
            # op[0] == empty
            s = set()
    else:
        op[1] = int(op[1])
        if op[0] == 'add':
            s.add(op[1])
        elif op[0] == 'remove':
            if op[1] in s:
                s.discard(op[1])
        elif op[0] == 'check':
            if op[1] in s:
                print(1)
            else:
                print(0)
        elif op[0] == 'toggle':
            if op[1] in s:
                s.discard(op[1])
            else:
                s.add(op[1])