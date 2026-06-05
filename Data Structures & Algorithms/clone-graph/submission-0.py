"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        mapp = {}
        seen = set()

        def dfs(node):
            seen.add(node)

            mapp[node] = Node(node.val)
            for nei in node.neighbors:
                if nei not in seen:
                    dfs(nei)

        dfs(node) # creates all notes and the hashmap
        
        for key, val in mapp.items():
            for ne in key.neighbors:
                val.neighbors.append(mapp[ne])

        return mapp[node]
