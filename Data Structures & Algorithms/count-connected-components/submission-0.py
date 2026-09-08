from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        M = defaultdict(list)

        for u,v in edges:
            M[u].append(v)
            M[v].append(u)

        def dfs(i):
            if i in visited: return False
            visited.add(i)

            for j in M[i]:
                dfs(j)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count