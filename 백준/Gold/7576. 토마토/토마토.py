import sys
from collections import deque

input = sys.stdin.readline

def bfs(m, n, ground):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    q = deque([(i, j) for i in range(m) for j in range(n) if ground[i][j] == 1])

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and ground[nx][ny] == 0:
                ground[nx][ny] = ground[x][y] + 1
                q.append((nx, ny))

def calculate_days(m, n, ground):
    bfs(m, n, ground)  

    max_days = 0
    for row in ground:
        for value in row:
            if value == 0:  
                return -1
            max_days = max(max_days, value)

    return max_days - 1

n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(m)]

result = calculate_days(m, n, ground)
print(result)