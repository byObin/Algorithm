def solution(array, commands):
    answer = []

    for i, j, k in commands:
        cut_arr = array[i-1:j]
        cut_arr.sort()
        answer.append(cut_arr[k-1])
        
    return answer