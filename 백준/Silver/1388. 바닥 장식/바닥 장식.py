d = [-1, 1]

def dfs_stack(i, j):
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        if not visited[x][y]:
            visited[x][y] = True

            if ground[x][y] == '-':
                for dy in d:
                    ny = y + dy
                    if 0 <= ny < m and not visited[x][ny] and ground[x][ny] == ground[x][y]:
                        stack.append((x, ny))
            else:
                for dx in d:
                    nx = x + dx
                    if 0 <= nx < n and not visited[nx][y] and ground[nx][y] == ground[x][y]:
                        stack.append((nx, y))

n, m = map(int, input().split())
ground = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs_stack(i, j)
            cnt += 1
print(cnt)