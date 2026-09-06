# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# node can be descendant of itself

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = root
        def dfs(node):
            nonlocal ans
            if not node:
                return

            if node.val > p.val and node.val > q.val :
                dfs(node.left)
                print("Low")
            elif node.val < p.val and node.val < q.val:
                dfs(node.right)
                print("High")
            else:
                ans = node

        dfs(root)
        return ans
