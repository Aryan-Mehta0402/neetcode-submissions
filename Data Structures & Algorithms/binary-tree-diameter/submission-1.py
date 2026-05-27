# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, node: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height_finder(curr):
            if not curr:
                return 0
            
            left = height_finder(curr.left)
            right = height_finder(curr.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        height_finder(node)
        return self.diameter
