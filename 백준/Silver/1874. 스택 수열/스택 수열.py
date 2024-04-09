import sys

input = sys.stdin.readline
n = int(input())

i = 1
stack = []
answer = []
flag = True

for _ in range(n):
    num = int(input())
    while i <= num:
        stack.append(i)
        answer.append('+')
        i += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        flag = False
        break
 
if flag:
    for j in answer:
        print(j)
else:
    print('NO')