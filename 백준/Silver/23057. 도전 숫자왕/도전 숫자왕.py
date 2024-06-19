from itertools import combinations

n = int(input())
nums = list(map(int, input().split()))
m = sum(nums)

sums = set()

for i in range(1, n+1):
    for j in combinations(nums, i):
        sums.add(sum(j))

print(m - len(sums))