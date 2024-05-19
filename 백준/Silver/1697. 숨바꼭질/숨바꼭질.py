from collections import deque

def bfs(s):
    q = deque([s])

    while q:
        v = q.popleft()
        if v == k:
            return visited[k]

        for d in [-1, 1, v]:
            if 0 <= v + d <= max and not visited[v+d]:
                visited[v+d] = visited[v] + 1
                q.append(v+d)

max = 10 ** 5
n, k = map(int, input().split())
visited = [0] * (max+1)
print(bfs(n))
