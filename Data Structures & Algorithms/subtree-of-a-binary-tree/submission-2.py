# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], soot: Optional[TreeNode]) -> bool:
        # start matching from each node
        def match(root, soot):
            if not root and not soot:
                return True
            elif not root or not soot or root.val != soot.val:
                return False
            else:
                return (match(root.left, soot.left) 
                and match(root.right, soot.right))

        ans = False
        def dfs(node):
            nonlocal ans

            if not node:
                return 
            
            if ans:
                return
            
            if node.val == soot.val:
                ans = match(node, soot)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans

