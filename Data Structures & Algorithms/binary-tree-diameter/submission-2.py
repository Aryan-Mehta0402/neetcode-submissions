# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, node: Optional[TreeNode]) -> int:
        # diameter = left max + right max -> for each node
        dia = 0

        def depth(node):
            nonlocal dia 

            if not node:
                return 0
            
            dept = 1 + max(depth(node.left), depth(node.right))
            dia = max(dia, depth(node.left) + depth(node.right))
            return dept

        depth(root)
        return dia
