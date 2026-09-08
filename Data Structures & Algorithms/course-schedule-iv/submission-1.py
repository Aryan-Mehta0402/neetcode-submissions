from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        visited = set()
        M = defaultdict(set)

        for u, v in prerequisites:
            M[u].add(v)

        def dfs(i):
            if i in visited: return 
            visited.add(i)
            for j in M[i].copy():
                dfs(j)
                for k in M[j]:
                    M[i].add(k)
        
        N = [[False]*numCourses for _ in range(numCourses)]

        for i in range(numCourses):
            dfs(i)
            for j in M[i]:
                N[i][j] = True

        ans = []
        for i, j in queries:
            ans.append(N[i][j])

        return ans