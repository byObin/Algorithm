graph = {
    1 : [2, 3, 4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3],
}

# dfs_재귀, 사전식 순서로 방문
def recursive_dfs(v, discovered = []):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

print(f'recursive_dfs : {recursive_dfs(1)}')
# recursive_dfs : [1, 2, 5, 6, 7, 3, 4]

# dfs_스택, 사전식 순서 역순으로 방문(stack으로 구현했기 때문)
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

print(f'iterative_dfs : {iterative_dfs(1)}')
# itertative_dfs : [1, 4, 3, 5, 7, 6, 2]