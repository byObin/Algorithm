def solution(priorities, location):
    answer = 1
    
    while priorities:
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
        else:
            if location == 0:
                break
            priorities.pop(0)
            answer += 1 
        location = location - 1 if location > 0 else len(priorities) - 1
    return answer