n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

cnt = []

for r in range(0,n-7):
    for c in range(0,m-7):
        cnt1 = 0
        cnt2 = 0
        for i in range(r,r+8):
            for j in range(c,c+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        cnt1 += 1
                    if board[i][j] != 'B':
                        cnt2 += 1
                else:
                    if board[i][j] != 'B':
                        cnt1 += 1
                    if board[i][j] != 'W':
                        cnt2 += 1
        cnt.append(min(cnt1, cnt2))

print(min(cnt))