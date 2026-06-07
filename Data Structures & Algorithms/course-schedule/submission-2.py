from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        # detect cycles

        D = defaultdict(list)

        for u, v in prereq:
            D[u].append(v)

        seen = set()
        ind = True

        def dfs(node):
            nonlocal ind
            for nei in D[node]:
                if nei not in seen:
                    seen.add(nei)
                    path.add(nei)
                    dfs(nei)
                    path.remove(nei)
                else:
                    if nei in path:
                        ind = False
                        return
    
        for i in range(numCourses):
            if i not in seen:
                path = set()
                path.add(i)
                seen.add(i)
                dfs(i)

        return ind
