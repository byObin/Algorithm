from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

dx = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(test_graph):
    q = deque()
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 2:
                q.append((i, j))
                visited[i][j] = True

    while q:
        a, b = q.popleft()
        for nx, ny in dx:
            na, nb = nx + a, ny + b
            if 0 <= na < n and 0 <= nb < m and test_graph[na][nb] == 0 and not visited[na][nb]:
                test_graph[na][nb] = 2
                visited[na][nb] = True
                q.append((na, nb))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 0:
                cnt += 1

    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
space = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]
answer = 0

for (ax,ay), (bx, by), (cx, cy) in list(combinations(space, 3)):
    test_graph = [row[:] for row in graph]
    test_graph[ax][ay] = 1
    test_graph[bx][by] = 1
    test_graph[cx][cy] = 1

    answer = max(answer, bfs(test_graph))

print(answer)