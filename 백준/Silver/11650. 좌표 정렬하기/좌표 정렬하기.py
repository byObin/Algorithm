import sys

n = int(sys.stdin.readline())

points = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x,y))

points.sort(key = lambda x: (x[0], x[1]))

for i in points:
    print(i[0],i[1])