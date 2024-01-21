def solution(num_list):
    list_sum = 0
    mul_sum = 1
    
    for i in num_list:
        list_sum += i
        mul_sum *= i
    
    if mul_sum < list_sum**2 :
        return 1
    else:
        return 0