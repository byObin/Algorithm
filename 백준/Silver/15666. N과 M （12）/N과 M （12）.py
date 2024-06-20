from itertools import combinations_with_replacement

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

result = sorted(set(combinations_with_replacement(num, m)))

for i in result:
    print(*i)