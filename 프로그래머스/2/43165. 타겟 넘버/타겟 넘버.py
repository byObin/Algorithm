answer = 0

def DFS(idx, numbers, target, value):
# idx : 현재 숫자의 index, value : 현재까지 계산된 숫자의 합
    global answer       # global 변수로 선언해 재귀 호출 간 값 유지/업데이트
    n = len(numbers)
    if idx == n and target == value:    # 모든 숫자 처리(idx == n) + 현재 값이 타겟과 일치(target == value)
        answer += 1
        return
    if idx == n:                        # 모든 숫자 처리 후 타겟과 불일치하면 재귀호출 종료
        return
    
    # 현재 idx 숫자를 value에 더하고/빼고 다음 숫자로 넘어감
    DFS(idx+1, numbers, target, value+numbers[idx])
    DFS(idx+1, numbers, target, value-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    
    return answer