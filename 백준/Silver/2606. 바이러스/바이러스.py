from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = True
    cnt = 0
    while q:
        s = q.popleft()
        visited[s] = True
        for w in graph[s]:
            if not visited[w]:
                q.append(w)
                visited[w] = True
                cnt += 1
    return cnt


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(1))