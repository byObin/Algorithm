import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
dic = defaultdict(int)

for _ in range(n):
    name, state = map(str, input().split())
    dic[name] += 1

for i in sorted(dic, reverse=True):
    if dic.get(i) % 2 != 0:
        print(i)