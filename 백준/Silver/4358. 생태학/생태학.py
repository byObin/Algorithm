import sys
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
input = sys.stdin.readline

trees = defaultdict(int)

while True:
    tree = input().rstrip()
    if tree == '':
        break
    trees[tree] += 1

for i in sorted(trees):
    v = Decimal(f'{trees.get(i) / sum(trees.values()) * 100}')
    print(i, v.quantize(Decimal('1.0000'), rounding=ROUND_HALF_UP))