import sys
from collections import deque
input = sys.stdin.readline

def print_graph():
    for i in graph:
        print(' '.join(str(s) for s in i))

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    while q:
        a, b = q.popleft()
        for dx, dy in [(-1,0), (1,0),(0,-1),(0,1)]:
            nx, ny = a + dx, b + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 0:
                graph[nx][ny] = graph[a][b] + 1
                q.append((nx, ny))
                visited[nx][ny] = True

def find_target(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                x, y = i, j
                break
    return x,y

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 목표지점 위치 찾기
tx,ty = find_target(graph)
graph[tx][ty] = 0

# 목표지점에서 bfs로 거리 구하기
bfs(tx, ty)

# 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1
for q in range(n):
    for r in range(m):
        if graph[q][r] == 1 and not visited[q][r]:
            graph[q][r] = -1

print_graph()