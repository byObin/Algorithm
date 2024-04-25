from itertools import combinations

# 입력
n, m = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(n)]

# 초기화
house = []
store = []
chicken_distance = 9999

# 집, 치킨집 위치 추출
for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            house.append((i, j))
        elif town[i][j] == 2:
            store.append((i, j))

# 치킨집 조합별 최소 치킨 거리 계산
for chicken_comb in combinations(store, m):
    tmp = 0
    for h in house:
        # 해당 집에서 가까운 치킨거리 계산
        min_dis = 999
        for c in chicken_comb:
            dis = abs(h[0] - c[0]) + abs(h[1] - c[1])
            min_dis = min(min_dis, dis)
        tmp += min_dis

    #결과값 업데이트
    chicken_distance = min(chicken_distance, tmp)

print(chicken_distance)