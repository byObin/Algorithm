import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

t = int(input())
def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m or graph[i][j] != 1:
        return
    graph[i][j] = 0

    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)


for _ in range(t):
    m, n, k = map(int, input().split())

    graph = list([0] * m for _ in range(n))
    visited = list([0] * m for _ in range(n))

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    cnt = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)