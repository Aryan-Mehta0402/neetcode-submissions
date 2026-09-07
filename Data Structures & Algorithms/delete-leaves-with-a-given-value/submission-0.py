# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def removeLeafNodes(self, node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    
        if not node:
            return None

        node.left = self.removeLeafNodes(node.left, target)
        node.right = self.removeLeafNodes(node.right, target)
        
        if not node.left and not node.right and node.val == target:
            return None

        return node

