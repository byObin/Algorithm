import sys
import heapq
input = sys.stdin.readline

def dijkstra(s, dis):
    dis[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        cur_dis, now = heapq.heappop(q)
        if cur_dis > dis[now]:
            continue
        for n, weight in graph[now]:
            cost = cur_dis + weight
            if cost < dis[n]:
                dis[n] = cost
                heapq.heappush(q, (cost, n))

                
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 최단경로 탐색 전 무한대(inf)로 초기화
dis = [float('inf')] * (V+1)

dijkstra(K, dis)

for i in dis[1:]:
    if i != float('inf'):
        print(i)

    # i가 무한대인 경우 경로 존재 x
    else:
        print('INF')