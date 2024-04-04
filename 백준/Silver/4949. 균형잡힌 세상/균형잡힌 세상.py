import sys

input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == '.':
        break
    if line.count('(') != line.count(')') or line.count('[') != line.count(']'):
        print('no')
        continue
    
    b = ''

    for i in line:
        if i in '()[]':
            b += i
    
    while '()' in b or '[]' in b:
        if '()' in b:
            b = b.replace('()', '')
        if '[]' in b:
            b = b.replace('[]', '')
    
    if b == '':
        print('yes')
    else:
        print('no')