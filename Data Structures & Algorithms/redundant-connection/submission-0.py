from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        visiting = set()
        cycle = set()
        M = defaultdict(list)
        cs = -1

        for u, v in edges:
            M[u].append(v)
            M[v].append(u)

        def dfs(i, p):
            nonlocal cs

            if i in visiting:
                cs = i
                return False

            if i in visited:
                return True

            visiting.add(i)

            for j in M[i]:
                if j == p:
                    continue

                if not dfs(j, i):
                    cycle.add(tuple(sorted((i, j))))
                    if i == cs:
                        return True
                    return False

            visiting.remove(i)
            visited.add(i)
            return True

        dfs(1, -1)

        for i in range(len(edges) - 1, -1, -1):
            if tuple(sorted(edges[i])) in cycle:
                return edges[i]