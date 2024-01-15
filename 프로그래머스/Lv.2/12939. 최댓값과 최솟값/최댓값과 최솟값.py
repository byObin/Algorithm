def solution(s):
    answer = []
    for i in s.split(' '):
        answer.append(int(i))
    return str(min(answer)) + ' ' + str(max(answer))