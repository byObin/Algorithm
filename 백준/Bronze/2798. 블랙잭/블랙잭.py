from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

# 합이 m을 넘지 않는 카드 3장, 최대한 m에 가깝게
min_d = m

for i in combinations(card,3):
    if sum(i) <= m:
        min_d = min(m-sum(i),min_d)

print(m-min_d)