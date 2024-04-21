from collections import deque

n = int(input())

def bfs(x):
    visited = [False] * (n + 1)  # n + 1 크기의 방문 체크 배열 생성
    q = deque([(x, 0)])  # 큐에 초기 값과 연산 횟수 추가
    visited[x] = True  # 초기 값 방문 체크

    while q:
        tmp, cnt = q.popleft()

        if tmp == 1:  # 1에 도달하면 연산 횟수 반환
            return cnt

        # 3으로 나누기 연산
        if tmp % 3 == 0 and not visited[tmp // 3]:
            visited[tmp // 3] = True
            q.append((tmp // 3, cnt + 1))

        # 2로 나누기 연산
        if tmp % 2 == 0 and not visited[tmp // 2]:
            visited[tmp // 2] = True
            q.append((tmp // 2, cnt + 1))

        # 1 빼기 연산
        if tmp > 1 and not visited[tmp - 1]:  # tmp > 1 조건으로 범위 초과 방지
            visited[tmp - 1] = True
            q.append((tmp - 1, cnt + 1))
    
print(bfs(n))