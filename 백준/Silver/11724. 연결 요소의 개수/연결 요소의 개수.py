import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(v, visited, result):
    visited[v] = True
    result.append(v)
    for w in sorted(graph[v]):
        if not visited[w]:
            dfs(w, visited, result)
    return result

n, m = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (n+1)
result = []
cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, visited, result)
        cnt += 1

print(cnt)