def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break
            else:
                return False
                break                    
            
    if stack:
        return False
    else:
        return True