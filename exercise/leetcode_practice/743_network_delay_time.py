# https://leetcode.com/problems/network-delay-time/

from typing import List
from collections import defaultdict 
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 큐 변수 : [(소요시간, 정점)]
        q = [(0, k)]
        dist = defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while q:
            time, node = heapq.heappop(q)
            # 현재 노드가 dist에 없다면, 최단 거리를 기록
            if node not in dist:
                dist[node] = time
                # 현재 노드의 인접 노드를 순회하며, 대체 경로 alt를 계산
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(q, (alt, v))
        
        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1


# Solution 클래스의 인스턴스 생성
sol = Solution()

# input
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

# networkDelayTime 메서드 호출
print(sol.networkDelayTime(times, n, k))
# output 2