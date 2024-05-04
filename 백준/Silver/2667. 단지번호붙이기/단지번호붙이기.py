n = int(input())

ground = [list(input()) for _ in range(n)]

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= n or ground[i][j] != '1':
        return 0
    
    ground[i][j] = '0'
    size = 1
    size += dfs(i-1, j)
    size += dfs(i+1, j)
    size += dfs(i, j-1)
    size += dfs(i, j+1)
    return size
cnt = 0
houses = []
for i in range(n):
    for j in range(n):
        if ground[i][j] == '1':
            houses.append(dfs(i, j))
            cnt += 1
print(cnt)
print('\n'.join(map(str,sorted(houses))))