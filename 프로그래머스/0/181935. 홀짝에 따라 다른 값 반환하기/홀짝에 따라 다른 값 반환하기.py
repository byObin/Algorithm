def solution(n):
    answer = 0
    if n%2 == 1:
        return sum(i for i in range(1,n+1,2))
    else:
        return sum(i*i for i in range(2,n+1,2))