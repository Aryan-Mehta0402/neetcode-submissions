# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ctr = 0
        self.ans = 0

        def inorder(cur):
            if not cur:
                return 

            inorder(cur.left)

            self.ctr += 1

            if self.ctr == k:
                self.ans = cur.val
                return

            inorder(cur.right)
        inorder(root)
        return self.ans

