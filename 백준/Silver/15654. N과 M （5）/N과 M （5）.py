from itertools import permutations

n, m = map(int, input().split())
num = list(map(int, input().split()))

result = sorted(list(permutations(num, m)))

for i in result:
    print(*i)