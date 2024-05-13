import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

# 상하좌우 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, h, visited):
    visited[x][y] = True

    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and ground[nx][ny] > h:
            dfs(nx, ny, h, visited)

n = int(input())
ground = [list(map(int, input().split())) for _ in range(n)]
max_height = max(max(row) for row in ground)    # 땅의 최대 높이 계산
answer = 1              # 최소 한 개의 안전 구역이 항상 존재

for k in range(1, max_height + 1):
    visited = [[False] * n for _ in range(n)]
    safe = 0
    for i in range(n):
        for j in range(n):
            if ground[i][j] > k and not visited[i][j]:
                safe += 1
                dfs(i, j, k, visited)
    answer = max(answer, safe)

print(answer)