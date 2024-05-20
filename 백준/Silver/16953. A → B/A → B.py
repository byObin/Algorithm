from collections import deque

MAX = 10 ** 9

def bfs(n):
    q = deque([(n, 1)])     # (노드, 변환 횟수)
    while q:
        v, cnt = q.popleft()
        if v == b:
            return cnt
        for w in [v * 2, (v * 10) + 1]:
            if w <= MAX:
                q.append((w, cnt + 1))
    return -1    

a, b = map(int, input().split())
print(bfs(a))