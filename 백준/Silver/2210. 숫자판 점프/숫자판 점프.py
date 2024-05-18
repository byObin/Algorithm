dx = [-1, 1, 0, 0,]
dy = [0, 0, -1, 1]

def dfs(i, j, path):
    if len(path) == 6:
        if path not in result:
            result.append(path)
        return

    path = path + graph[i][j]

    for n in range(4):
        nx = i + dx[n]
        ny = j + dy[n]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, path)

graph = [list(map(str, input().split())) for _ in range(5)]
result = []

for i in range(5):
    for j in range(5):
        dfs(i, j, '')

print(len(result))