# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수 : [(가격, 정점, 남은 가능 경유지 수)]
        q = [(0, src, k)]

        # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
        while q:
            price, node, k = heapq.heappop(q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(q, (alt, v, k-1))
        return -1

# Solution 클래스의 인스턴스 생성
sol = Solution()

# input
n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 0

# findCheapestPrice 메서드 호출
print(sol.findCheapestPrice(n, flights, src, dst, k))
# output 500