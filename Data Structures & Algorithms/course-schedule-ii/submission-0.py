from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        # prerequisite -> course
        for course, pre in prerequisites:
            graph[pre].append(course)

        visiting = set()  # current recursion stack
        visited = set()   # fully processed
        order = []

        def dfs(course):
            if course in visiting:
                return False  # cycle

            if course in visited:
                return True

            visiting.add(course)

            for nei in graph[course]:
                if not dfs(nei):
                    return False

            visiting.remove(course)
            visited.add(course)
            order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order[::-1]