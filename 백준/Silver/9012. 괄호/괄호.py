n = int(input())


for _ in range(n):
    stack = []
    isVPS = True
    for c in input():
        if c==')':
            if len(stack)>0:
                stack.pop()
            else:
                isVPS = False
                break
        else:
            stack.append(c)
           
    if len(stack)>0:
        isVPS = False

    print('YES' if isVPS else 'NO')