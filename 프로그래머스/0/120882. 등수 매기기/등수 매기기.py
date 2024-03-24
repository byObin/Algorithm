def solution(score):
    avg_score = []
    answer = []
    
    for i in score:
        avg = (i[0]+i[1])/2
        avg_score.append(avg)
        
    for j in range(len(avg_score)):
        rank = 1
        for k in range(len(avg_score)):
            if avg_score[j] < avg_score[k]:
                rank += 1
        answer.append(rank)
    
    return answer