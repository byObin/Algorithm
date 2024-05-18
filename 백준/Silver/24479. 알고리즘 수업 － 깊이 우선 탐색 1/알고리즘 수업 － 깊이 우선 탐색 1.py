import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs_stack(start):
    stack = [start]
    order = [0] * (n + 1)
    cnt = 1

    while stack:
        s = stack.pop()
        if not visited[s]:
            visited[s] = True
            order[s] = cnt
            cnt += 1
            for w in sorted(graph[s], reverse=True):
                if not visited[w]:
                    stack.append(w)
    return order

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)


for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

order = dfs_stack(r)

for i in range(1, n+1):
    print(order[i])
