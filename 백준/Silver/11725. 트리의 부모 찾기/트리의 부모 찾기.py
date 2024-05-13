import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v):
    for w in graph[v]:
        if visited[w] == 0:
            visited[w] = v  # 노드 방문 경로 기록
            dfs(w)

n = int(input())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

for _ in range(1, n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# DFS 시작 노드 지정
dfs(1)

for i in range(2, n+1):
    print(visited[i])

# visited = [0, 6, 4, 6, 1, 3, 1, 4]