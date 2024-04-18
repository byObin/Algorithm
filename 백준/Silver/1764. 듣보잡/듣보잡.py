import sys

input = sys.stdin.readline

n, m = map(int, input().split())

name_dic = {}

for i in range(n+m):
    p = input().strip()
    if p in name_dic:
        name_dic[p] += 1
    else:
        name_dic[p] = 1

result = []
count = 0
for k, v in name_dic.items():
    if v == 2:
        result.append(k)
        count += 1

print(count)

for j in sorted(result):
    print(j)
