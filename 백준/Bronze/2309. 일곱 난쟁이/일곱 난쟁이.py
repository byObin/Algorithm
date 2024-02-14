from itertools import combinations

h=[int(input()) for _ in range(9)]

for j in combinations(h,7):
        if sum(j) == 100:
            for k in sorted(j):
                 print(k)
            break