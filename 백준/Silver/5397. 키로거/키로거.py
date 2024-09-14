import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    str1 = []
    str2 = []
    for i in input().rstrip():
        if i == '-':
            if str1:
                str1.pop()
        elif i == '<':
            if str1:
                str2.append(str1.pop())
        elif i == '>':
            if str2:
                str1.append(str2.pop())
        else:
            str1.append(i)
    
    str1.extend(reversed(str2))
    print(''.join(str1))