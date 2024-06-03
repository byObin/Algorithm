import sys
input = sys.stdin.readline

# 분할 정복 함수
def count_paper(x, y, n):
    global white_cnt, blue_cnt
    color = paper[x][y]
    same_color = True
    # 현재 영역의 모든 셀이 같은 색인지 확인
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                same_color = False
                break
        if not same_color:
            break
    
    if same_color:  # same_color가 True면 카운트 증가
        if color == 0:
            white_cnt += 1
        else:
            blue_cnt += 1
    else: # same_color가 False면
        # 현재 영역을 네개의 작은 영역으로 분할
        half = n // 2
        count_paper(x, y, half)
        count_paper(x, y+half, half)
        count_paper(x+half, y, half)
        count_paper(x+half, y+half, half)


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white_cnt = 0
blue_cnt = 0

count_paper(0, 0, n)

print(white_cnt)
print(blue_cnt)