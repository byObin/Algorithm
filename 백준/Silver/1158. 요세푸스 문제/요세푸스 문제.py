from collections import deque

n, k = map(int, input().split())
q1 = deque([i for i in range(1,n+1)])
answer = []

for _ in range(n):
    for _ in range(k-1):
        q1.append(q1.popleft())
    answer.append(q1.popleft())

print('<',end='')
print(*answer, sep=', ', end='>')