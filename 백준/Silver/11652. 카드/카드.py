import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
hash_map = defaultdict(int)
for _ in range(n):
    hash_map[int(input())] += 1

print(sorted(hash_map.items(), key=lambda x : (-x[1], x[0]))[0][0])