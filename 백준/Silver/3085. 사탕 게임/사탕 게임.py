n = int(input())

candy = [list(input()) for _ in range(n)]

def candy_cnt(candy):
    max_cnt = 1  
    for k in range(0,n):
        cnt = 1
        for l in range(1,n):
            if candy[k][l] == candy[k][l-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
        
        cnt = 1
        for l in range(1,n):
            if candy[l][k] == candy[l-1][k] :
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    return max_cnt



answer = 0


for i in range(n):
    for j in range(n):
        if j + 1 < n: # 열 범위 체크
            # 인접한 것끼리 바꿔주기
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            cnt = candy_cnt(candy)
            answer = max(answer, cnt)
            # 바꾼 것 원래대로 돌려놓기
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

        if i + 1 < n: # 행 범위 체크
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            cnt = candy_cnt(candy)
            answer = max(answer, cnt)
            # 바꾼 것 원래대로 돌려놓기
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]



print(answer)