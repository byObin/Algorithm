import sys
from collections import deque
input = sys.stdin.readline

def find_location():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'I':
                tx, ty = i, j
                break
    return tx, ty

def bfs(x, y):
    d = [(-1,0),(1,0),(0,-1),(0,1)]
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0
    while q:
        cx, cy = q.popleft()
        for dx, dy in d:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'X' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

                if graph[nx][ny] == 'P':
                    cnt += 1

    return cnt        

n, m = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 도연이의 위치 찾기
x, y = find_location()

# 도연이가 만날 수 있는 친구 수 구하기
result = bfs(x, y)

# 결과 출력
if result == 0:
    print('TT')
else:
    print(result)