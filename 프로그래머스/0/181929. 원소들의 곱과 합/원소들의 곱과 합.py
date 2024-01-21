def solution(num_list):
    answer = 0
    mul_sum = 1
    
    for i in num_list:
        mul_sum *= i
    
    if mul_sum < (sum(num_list)**2):
        return 1
    else:
        return 0