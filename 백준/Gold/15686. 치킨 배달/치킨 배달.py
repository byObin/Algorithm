from itertools import combinations

n, m = map(int, input().split())

town = [list(map(int, input().split())) for _ in range(n)]
house = []
store = []

chicken_distance = 9999

for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            house.append([i, j])
        elif town[i][j] == 2:
            store.append([i, j])

for i in combinations(store, m):
    tmp = 0
    for h in house:
        c_dis = 999
        for j in range(m):
            c_dis = min(c_dis, abs(h[0] - i[j][0]) + abs(h[1] - i[j][1]))
        tmp += c_dis
    chicken_distance = min(chicken_distance, tmp)

print(chicken_distance)