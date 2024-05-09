import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def findColors(n, board):
    visited = [list([False] * n) for _ in range(n)]
    colors = {'R' : 0, 'G' : 0, 'B' : 0}

    def dfs(i, j, color):
        if i < 0 or i >= n or j < 0 or j >= n or board[i][j] != color or visited[i][j]:
            return
        
        visited[i][j] = True
        
        dfs(i+1, j, color)
        dfs(i-1, j, color)
        dfs(i, j+1, color)
        dfs(i, j-1, color)

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                color = board[i][j]
                dfs(i, j, color)
                colors[color] += 1

    return sum(colors.values())

n = int(input())
board = [list(map(str, input().rstrip())) for _ in range(n)]
result = []

result.append(str(findColors(n, board)))

for i in range(n):
    for j in range(n):
            if board[i][j] == 'G':
                board[i][j] = 'R'

result.append(str(findColors(n, board)))

print(' '.join(result))