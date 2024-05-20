from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    board[x][y] += 1
    while q:
        m, n = q.popleft()
        if m == tx and n == ty:
            return board[m][n] - 1
        
        for dx, dy in [(2,-1), (1,-2), (2,1), (1,2), (-2,1), (-1,2), (-2,-1), (-1,-2)]:
            nx, ny = m + dx, n + dy
            if 0 <= nx < i and 0 <= ny < i and board[nx][ny] == 0:
                board[nx][ny] = board[m][n] + 1
                q.append((nx, ny))

t = int(input())
for _ in range(t):
    i = int(input())
    x, y = map(int, input().split())
    tx, ty = map(int, input().split())
    
    board = [[0] * i for _ in range(i)]

    print(bfs(x, y))