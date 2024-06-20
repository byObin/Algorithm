from itertools import permutations

n, m = map(int, input().split())
num = list(map(int, input().split()))

result = sorted(set(permutations(num, m)))

for i in result:
    print(*i)