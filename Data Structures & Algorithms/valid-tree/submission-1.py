from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # conditions for a tree
        # no. of edges = n - 1 & one connected component
        if len(edges) != n - 1:
            return False
            
        M = defaultdict(list)
        visited = set()

        for u, v in edges:
            M[u].append(v)
            M[v].append(u)

        count = 0
        def dfs(i):
            nonlocal count

            if i in visited:
                return 

            visited.add(i)
            count += 1

            for j in M[i]:
                dfs(j)

        dfs(0)
        return count == n 