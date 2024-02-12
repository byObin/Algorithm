import heapq as hq
import sys


# input보다 readline이 빠르기 때문에 입력값이 많은 경우에는 readline을 사용
input = sys.stdin.readline
n = int(input())

arr = []

for _ in range(n):
    x = int(input())
    if x:
        hq.heappush(arr, (abs(x),x))
    else:
        print(hq.heappop(arr)[1] if arr else 0)