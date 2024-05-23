from collections import deque
import sys

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for dx, dy, dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append((nx, ny, nz))

def calculate_days():
    bfs()

    max_days = 0

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return -1
                max_days = max(max_days, graph[i][j][k])
    
    return max_days - 1

m, n, h = map(int, input().split())
graph = []
queue = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().strip().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append([i, j, k])
    graph.append(tmp)

result = calculate_days()

print(result)