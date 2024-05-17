def dfs(v, cnt):
    visited[v] = True
    if v==b:
        return cnt
    
    for w in graph[v]:
        if not visited[w]:
            result = dfs(w, cnt+1)
            if result is not None:
                return result
    return
    
# 입력
n = int(input())
a, b = map(int, input().split())
m = int(input())

# 그래프 생성
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# DFS 실행
result = dfs(a, 0)

if result is not None:
    print(result)
else:
    print(-1)