from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]


def bfs(graph, x, y):
    q = deque([(0, 0)])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]

print(bfs(maze, 0, 0))