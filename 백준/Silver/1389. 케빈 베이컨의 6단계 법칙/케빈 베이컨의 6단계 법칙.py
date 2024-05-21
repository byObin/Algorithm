from collections import deque

def bfs(v, t):
    depth = 0
    q = deque([(v, depth)])
    visited[v] = True
    while q:
        n, cnt = q.popleft()
        if n == t:
            break
        for w in graph[n]:
            if not visited[w]:
                q.append((w, cnt + 1))
                visited[w] = True
    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

friends = [[] for _ in range(n+1)]
for j in range(1,n+1):
    results = []
    for i in range(1,n+1):
        visited = [False] * (n+1)
        results.append(bfs(j, i))
    friends[j].append(sum(results))

print(friends.index(min(friends[1:])))