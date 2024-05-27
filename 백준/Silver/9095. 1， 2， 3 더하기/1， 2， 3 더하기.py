from itertools import product

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [1,2,3]
    cnt = 0
    for i in range(1, n+1):
        for j in list(product(nums, repeat=i)):
            if sum(j) == n:
                cnt += 1
    print(cnt)