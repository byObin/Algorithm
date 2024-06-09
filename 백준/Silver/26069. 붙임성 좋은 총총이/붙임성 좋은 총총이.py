import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
dancing_people = defaultdict(int)

for _ in range(n):
    a, b = input().rstrip().split()
    if a == 'ChongChong' or  b == 'ChongChong':
        dancing_people[a] += 1
        dancing_people[b] += 1
    elif a in dancing_people or b in dancing_people:
        dancing_people[a] += 1
        dancing_people[b] += 1

print(len(dancing_people))     