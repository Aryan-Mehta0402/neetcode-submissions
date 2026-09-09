from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        M = defaultdict(list)

        for i, eq in enumerate(equations):
            u , v = eq
            M[u].append([v, values[i]])
            M[v].append([u, 1/values[i]])

        def bfs(st, tar):
            if st not in M or tar not in M:
                return -1
            q, visited = deque(), set()
            q.append([st, 1])

            while q:
                n, w = q.popleft()
                if tar == n:
                    return w
                for nei, we in M[n]:
                    if nei not in visited:
                        q.append([nei, w*we])
                        visited.add(nei)

            return -1

        return [bfs(u, v) for u, v in queries]