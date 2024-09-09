from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

dx = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x, y, test_graph):
    q = deque([(x, y)])
    g = test_graph
    visited[x][y] = True
    while q:
        a, b = q.popleft()
        for nx, ny in dx:
            na, nb = nx + a, ny + b
            if 0 <= na < n and 0 <= nb < m and g[na][nb] == 0 and not visited[na][nb]:
                g[na][nb] = 2
                visited[na][nb] = True
                q.append((na, nb))
    return g


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
space = []
answer = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            space.append((i, j))

for (ax,ay), (bx, by), (cx, cy) in list(combinations(space, 3)):
    test_graph = deepcopy(graph)
    test_graph[ax][ay] = 1
    test_graph[bx][by] = 1
    test_graph[cx][cy] = 1

    
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 2 and not visited[i][j]:
                bfs(i, j, test_graph)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 0:
                cnt += 1
    answer.append(cnt)

print(max(answer))