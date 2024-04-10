import sys
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

flat_ground = [h for r in ground for h in r]

h_counter = Counter(flat_ground)

min_time = sys.maxsize
optimal_h = 0

for i in range(257):
    exc_block = lack_block = 0

    for h, c in h_counter.items():
        if h > i:
            exc_block += (h - i) * c
        elif h < i:
            lack_block += (i - h) * c
    
    if exc_block + b >= lack_block:
        time = (exc_block * 2) + lack_block
        if time <= min_time:
            min_time = time
            optimal_h = i

print(min_time, optimal_h)