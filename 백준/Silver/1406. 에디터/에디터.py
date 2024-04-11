import sys

input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = []
m = int(input())

for _ in range(m):
    op = input().split()
    if op[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif op[0] == 'D':
        if s2:
            s1.append(s2.pop())
    elif op[0] == 'B':
        if s1:
            s1.pop()
    else:
        s1.append(op[1])

s1.extend(reversed(s2))
print(''.join(s1))

