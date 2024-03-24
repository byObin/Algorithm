import sys
import math

def my_round(x):
    return math.trunc(x + 0.5)

n = int(input())
scores = [int(line) for line in sys.stdin.readlines()]

scores.sort()

if len(scores) == 0:
    print(0)
else:
    a = my_round(n * 0.15)
    if a == 0:
        print(my_round(sum(scores)/len(scores)))
    else:
        print(my_round(sum(scores[a:-a])/len(scores[a:-a])))