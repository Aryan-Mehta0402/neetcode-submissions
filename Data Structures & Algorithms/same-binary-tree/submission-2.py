# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.sig = True

        def dfs(f, s):
            if self.sig == False:
                return
            if not f and not s:
                return
            elif not f or not s:
                self.sig = False
                return

            if f.val != s.val:
                self.sig = False

            dfs(f.left, s.left)
            dfs(f.right, s.right)
        dfs(p, q)
        return self.sig

        