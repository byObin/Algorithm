import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs_stack(v):
    stack = [v]
    while stack:
        s = stack.pop()
        for w in graph[s]:
            if visited[w] == 0:
                visited[w] = s  # 노드 방문 경로 기록
                stack.append(w)

n = int(input())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

for _ in range(1, n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# DFS 시작 노드 지정
dfs_stack(1)

for i in range(2, n+1):
    print(visited[i])
