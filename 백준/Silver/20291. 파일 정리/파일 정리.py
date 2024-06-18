import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for _ in range(n):
    name, type = input().rstrip().split('.')
    if type in dic:
        dic[type] += 1
    else:
        dic[type] = 1

for k, v in sorted(dic.items()):
    print(k, v)