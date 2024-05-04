import sys
from collections import deque
input = sys.stdin.readline

def dfs(v, visited, dis):
    dis.append(v)
    visited[v] = True
    for w in sorted(graph[v]):
        if not visited[w]:
            dfs(w, visited, dis)
    return dis

def bfs(v, visited):
    q = deque([v])
    dis = []
    visited[v] = True
    while q:
        v = q.popleft()
        dis.append(v)
        for w in sorted(graph[v]):
            if not visited[w]:
                visited[w] = True
                q.append(w)
    return dis




n, m, v = map(int, input().split())
graph = {i : [] for i in range(1,n+1)}
visited = [False] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dis = []

print(' '.join(map(str,dfs(v, visited, dis))))
# print(visited)
visited = [False] * (n+1)
print(' '.join(map(str, bfs(v, visited))))
