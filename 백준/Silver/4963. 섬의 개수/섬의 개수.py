import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(i, j):
    # 상하좌우, 대각선 방향벡터
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    stack = [(i, j)]
    graph[i][j] = 0

    while stack:
        x, y = stack.pop()
        for n in range(8):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                stack.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)