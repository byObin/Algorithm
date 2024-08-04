import sys
sys.setrecursionlimit(10 ** 7)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True
    global size
    for nx, ny in zip(dx, dy):
        cx = x + nx
        cy = y + ny
        if 0 <= cx < n and 0 <= cy < m and graph[cx][cy] == 1 and not visited[cx][cy]:
           bfs(cx, cy)
           size += 1
    return size


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0
max_size = 0
size = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            size = 1
            max_size = max(max_size, bfs(i, j))

print(cnt)
print(max_size)