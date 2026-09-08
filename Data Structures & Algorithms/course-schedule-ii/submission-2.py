from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        M = defaultdict(list)

        for u, v in prerequisites:
            M[u].append(v)

        ans = []
        visited, visiting = set(), set()

        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)

            for j in M[i]:
                if not dfs(j):
                    return False
            visiting.remove(i)
            visited.add(i)
            ans.append(i)
            return True
        
        for c in range(numCourses):
            if c not in visited:
                if not dfs(c):
                    return []
        return ans
