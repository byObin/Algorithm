import sys

input = sys.stdin.readline

n = int(input())

s = [0]

for i in range(n):
    num = int(input())
    if int(num) == 0:
        s.pop()
    else:
        s.append(num)

print(sum(s))