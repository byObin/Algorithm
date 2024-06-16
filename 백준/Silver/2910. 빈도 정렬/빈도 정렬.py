from collections import defaultdict

n, c = map(int, input().split())
nums = list(map(int, input().split()))
dic = defaultdict(int)
for i in nums:
    dic[i] += 1

sorted_dic = sorted(dic.items(), key = lambda x: (-x[1], list(dic.keys()).index(x[0])))

for i, j in sorted_dic:
    for _ in range(j):
        print(i, end=' ')