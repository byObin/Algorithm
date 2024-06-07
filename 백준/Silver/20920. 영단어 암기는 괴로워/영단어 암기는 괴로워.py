import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
hash_map = defaultdict(int)

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:    
        hash_map[word] += 1

my_words = sorted(hash_map, key = lambda x : (-hash_map[x], -len(x), x))

print('\n'.join(my_words))