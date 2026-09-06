"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def checkk(self, x, y, size, grid):
        typ = grid[x][y]

        for i in range(x, x + size):
            for j in range(y, y + size):
                if grid[i][j] != typ:
                    return False, typ

        return True, typ

    def construct(self, grid: List[List[int]]) -> 'Node':
        lenn = len(grid)
        half = lenn // 2

        ans, typ = self.checkk(0, 0, lenn, grid)

        if ans:
            return Node(typ, True)

        topLeft = [row[:half] for row in grid[:half]]
        topRight = [row[half:] for row in grid[:half]]
        bottomLeft = [row[:half] for row in grid[half:]]
        bottomRight = [row[half:] for row in grid[half:]]

        return Node(
            True,
            False,
            self.construct(topLeft),
            self.construct(topRight),
            self.construct(bottomLeft),
            self.construct(bottomRight)
        )