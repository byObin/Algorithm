d = [-1, 1]

def dfs(i, j):
    visited[i][j] = True
    if ground[i][j] == '-':
        for y in range(2):
            ny = j + d[y]
            if 0 <= ny < m and not visited[i][ny] and ground[i][ny] == ground[i][j]:
                dfs(i, ny)
    else:
        for x in range(2):
            nx = i + d[x]
            if 0 <= nx < n and not visited[nx][j] and ground[nx][j] == ground[i][j]:
                dfs(nx, j)

n, m = map(int, input().split())
ground = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1
print(cnt)