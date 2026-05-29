# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, node: Optional[TreeNode]) -> bool:
       
        def dfs(cur, l ,r):
            if not cur:
                return True
            if not l < cur.val < r:
                return False

            return dfs(cur.left, l, cur.val) and dfs(cur.right, cur.val, r)

        return dfs(node, -1*float("inf"), float("inf"))

        
            