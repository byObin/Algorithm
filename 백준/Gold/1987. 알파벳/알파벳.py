import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j, cnt):
    global max_len
    max_len = max(max_len, cnt)

    # 상하좌우로 이동
    for n in range(4):
        nx, ny = i + dx[n], j + dy[n]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in visited:
            # 백트래킹 : 경로에 포함시키기
            visited.add(board[nx][ny])
            dfs(nx, ny, cnt + 1)
            # 백트래킹 : 경로에서 제거하기
            visited.remove(board[nx][ny])

r, c = map(int, input().split())
board = list()
for _ in range(r):
    board.append(list(input()))

max_len = 0
visited = set()
visited.add(board[0][0])
dfs(0, 0, 1)
print(max_len)