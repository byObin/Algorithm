import sys
import heapq
input = sys.stdin.readline

def dijkstra(s, dis):
    dis[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        cur_dis, now = heapq.heappop(q)
        for n, weight in graph[now]:
            cost = cur_dis + weight
            if dis[n] == -1 or cost < dis[n]:
                dis[n] = cost
                heapq.heappush(q, (cost, n))

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# -1로 초기화해 최단경로 모르는 상태 표시
dis = [-1] * (V+1)
q = []

dijkstra(K, dis)

for i in dis[1:]:
    # i가 -1일 경우 최단경로 탐색되지 않음 = 경로 존재 x
    if i != -1:
        print(i)
    else:
        print('INF')