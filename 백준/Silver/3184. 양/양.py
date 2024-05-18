def dfs(i, j):
    stack = [(i, j)]
    wolf = 0
    sheep = 0

    while stack:
        x, y = stack.pop()
        if not visited[x][y]:
            visited[x][y] = True
            if graph[x][y] == 'v':
                wolf += 1
            elif graph[x][y] == 'o':
                sheep += 1
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#' and not visited[nx][ny]:
                    stack.append((nx, ny))

    return (wolf, sheep)

r, c = map(int, input().split())
graph = [(list(input().rstrip())) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
final_wolf = 0
final_sheep = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'v' and not visited[i][j] or graph[i][j] == 'o' and not visited[i][j]:
            w, s = dfs(i, j)
            if s > w:
                final_sheep += s
            else:
                final_wolf += w

print(final_sheep, final_wolf)