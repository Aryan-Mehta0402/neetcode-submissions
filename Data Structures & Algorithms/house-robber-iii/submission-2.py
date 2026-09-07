# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {None: 0}

        def robb(node):
            if node in cache:
                return cache[node]

            if not node:
                return 0

            l = node.left
            if node.left:
                ll = l.left
                lr = l.right
            else: 
                ll, lr = None, None

            r = node.right
            if node.right:
                rl = r.left
                rr = r.right
            else:
                rl, rr = None, None

            cache[node] = max(node.val + robb(ll) + robb(lr) + robb(rl) + robb(rr), 
                                robb(l) + robb(r))
            return cache[node]

        return robb(root)