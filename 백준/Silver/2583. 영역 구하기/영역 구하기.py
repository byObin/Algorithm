import sys
sys.setrecursionlimit(10 ** 5)

def dfs(i, j):
    if i < 0 or i >= m or j < 0 or j >= n or graph[i][j] != 0:
        return 0
    size = 1
    graph[i][j] = 1
    
    size += dfs(i+1, j)
    size += dfs(i-1, j)
    size += dfs(i, j+1)
    size += dfs(i, j-1)
    
    return size

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            graph[i][j] = 1
cnt = 0
result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(dfs(i, j))
            cnt += 1

print(cnt)
print(' '.join(str(i) for i in sorted(result)))