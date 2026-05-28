# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], soot: Optional[TreeNode]) -> bool:
        
        def same(f, s):
            if not f and not s:
                return True

            elif not f or not s:
                return False
            
            elif f.val != s.val:
                return False
            
            return same(f.left, s.left) and same(f.right, s.right)
        
        if not root:
            return False
        
        if same(root, soot):
            return True

        return self.isSubtree(root.left, soot) or self.isSubtree(root.right, soot)
        
