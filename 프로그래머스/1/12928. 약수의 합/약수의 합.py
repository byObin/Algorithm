def solution(n):
    answer = 0
    num = []
    for i in range(1,n+1):
        if n%i == 0:
            num.append(i)
    return sum(num)