import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(node):
    global max_dia
    # 현재 노드에서 자식 노드로 가는 경로 중 가장 긴 경로 두개 저장
    long_one, long_two = 0, 0
    # 인접 노드 탐색
    for cn, cw in tree[node]:
        if not visited[cn]:
            visited[cn] = True
            path_len = dfs(cn) + cw
            
            if path_len > long_one:
                long_one, long_two = path_len, long_one
            elif path_len > long_two:
                long_two = path_len
    
    max_dia = max(max_dia, long_one + long_two)
    return long_one


# 입력
n = int(input())
tree = [[] for _ in range(n+1)]

# tree[노드번호] = (부모or자식노드번호, 가중치)
for _ in range(n-1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

visited = [False] * (n+1)
max_dia = 0

# 루트 노드에서 탐색 시작
visited[1] = True
dfs(1)

print(max_dia)