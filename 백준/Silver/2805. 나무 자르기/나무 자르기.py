import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2

    log_sum = 0     # 현재 높이에서 벌목 나무 합
    for i in trees:
        if i >= mid:
            log_sum += i - mid
    
    if log_sum >= m:
        start = mid + 1
    else:
        end = mid -1

print(end)