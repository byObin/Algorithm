from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    n = len(numbers)
    
    q.append([numbers[0], 0])
    q.append([-1 * numbers[0], 0])

    while q:
        tmp, idx = q.popleft()  # q의 원소들 뽑아서 확인
        idx += 1
        
        if idx < n:             # 아직 모든 원소 사용 x
            q.append([tmp + numbers[idx], idx])
            q.append([tmp - numbers[idx], idx])
        else:                   # 모든 원소 사용 완료  
            if tmp == target:   # 조합으로 target값 만들어졌는지 확인
                answer += 1
    return answer