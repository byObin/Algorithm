stat = input()

pipe = 0
cnt = 0

stack = []

for i in stat:
    if i == '(':    
        pipe += 1
    else:           
        if stack[-1] == '(':    
            pipe -= 1
            cnt += pipe
        else:                   
            pipe -= 1
            cnt += 1
    stack.append(i)

print(cnt)
