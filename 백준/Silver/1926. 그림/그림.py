import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    size = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny <m and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                size += 1
    return size

def main():
    global n, m, graph, visited
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    max_size = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                cnt += 1
                max_size = max(max_size, bfs(i, j))

    print(cnt)
    print(max_size)

if __name__ == "__main__":
    main()