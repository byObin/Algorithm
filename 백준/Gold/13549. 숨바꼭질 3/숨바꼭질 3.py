import sys
from collections import deque
input = sys.stdin.readline

def bfs(now, target):
    q = deque([now])
    time[now] = 0   # 방문 처리

    while q:
        x = q.popleft()
        # 현재 위치가 target(동생 위치)와 일치하면 시간 리턴
        if x == target:
            return time[x]
        
        for nx in (x-1,x+1,x*2):
            if 0<= nx < limit and time[nx] == -1:
                if nx == 2*x:
                    time[nx] = time[x]
                    # 시간 증가하지 않았으므로 q 맨 앞 추가
                    q.appendleft(nx)    
                else:
                    # 시간 1 증가, q 맨 뒤에 추가
                    time[nx] = time[x] +1
                    q.append(nx)


# 현재 위치 p, 목표 위치 t 입력 받기
p, t = map(int, input().split())
limit = 100001
time = [-1] * limit     # 방문 체크 및 시간 저장

print(bfs(p, t))