import sys
input = sys.stdin.readline

def dfs(i, j, path):
    if len(path) == 6:
        result.add(path)
        return

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = i + dx
        ny = j + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, path + graph[i][j])

graph = [list(map(str, input().split())) for _ in range(5)]
result = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, '')

print(len(result))