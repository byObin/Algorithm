import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(r, cnt):
    visited[r] = True
    order[r] = cnt
    cnt += 1
    for w in sorted(graph[r], reverse=True):
        if not visited[w]:
            cnt = dfs(w, cnt)
    return cnt

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
order = [0] * (n+1)
cnt = 1

dfs(r, cnt)

for i in range(1, n+1):
    print(order[i])