import sys
input = sys.stdin.readline

def dfs(node, cnt):
    visited[node] = True
    for n in tree[node]:
        if not visited[n]:
            cnt = dfs(n, cnt+1)
    return cnt

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    tree = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(m):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    visited[1] = True

    print(dfs(1,0))