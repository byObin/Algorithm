import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(i, j):
    visited[i][j] = True
    cnt = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = i + dx
        ny = j + dy
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[i][j] == graph[nx][ny]:
            cnt += dfs(nx, ny)
    return cnt

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
w = []
b = []

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                w.append(dfs(i, j))
            else:
                b.append(dfs(i, j))
w_sum = 0
for k in w:
    w_sum += k ** 2

b_sum = 0
for l in b:
    b_sum += l ** 2

print(w_sum, b_sum)