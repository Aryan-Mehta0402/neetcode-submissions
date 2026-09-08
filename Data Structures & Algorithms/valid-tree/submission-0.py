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

        def dfs(i):
            if i in visited:
                return 

            visited.add(i)

            for j in M[i]:
                dfs(j)

        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count == 1