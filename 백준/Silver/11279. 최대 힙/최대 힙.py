import heapq as hq
import sys

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(-hq.heappop(heap))
        else:
            print(0)
    else:
        hq.heappush(heap, -x)