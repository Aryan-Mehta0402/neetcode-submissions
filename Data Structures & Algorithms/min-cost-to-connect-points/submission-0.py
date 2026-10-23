import heapq as hp

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[] for x in range(n)]

        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                adj[i].append([j, dist])

        heap = [(0, 0, -1)]  # weight, node, parent
        vis = set()
        summ = 0

        while heap:
            w, t, f = hp.heappop(heap)

            if t in vis:
                continue

            vis.add(t)
            summ += w

            for n, weight in adj[t]:
                if n not in vis:
                    hp.heappush(heap, (weight, n, t))

        return summ
