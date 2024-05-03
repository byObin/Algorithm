from collections import deque

def recursive_dfs(graph, v, visited, result):
    visited[v] = True
    result.append(v)
    for w in sorted(graph[v]):
        if not visited[w]:
            recursive_dfs(graph, w, visited, result)
    return result

def iterative_bfs(graph, v, visited):
    q = deque([v])
    result = []
    visited[v] = True
    while q:
        v = q.popleft()
        result.append(v)
        for w in sorted(graph[v]):  
            if not visited[w]:
                visited[w] = True
                q.append(w)
    return result

n, m, v = map(int, input().split())

graph = {i : [] for i in range(1, n+1)} 

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited_d = [False] * (n+1)
visited_b = [False] * (n+1)
result = []

print(' '.join(map(str, (recursive_dfs(graph, v, visited_d, result)))))
print(' '.join(map(str, (iterative_bfs(graph, v, visited_b)))))