import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))

        # Nodes are 1-indexed, so make distance array of size n+1
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        pq = [(0, k)]  # (distance, node)

        while pq:
            curr_dist, node = heapq.heappop(pq)

            # Ignore stale entries
            if curr_dist > dist[node]:
                continue

            for nei, wt in graph[node]:
                new_dist = curr_dist + wt

                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(pq, (new_dist, nei))

        ans = max(dist[1:])   # Ignore index 0
        return -1 if ans == float("inf") else ans