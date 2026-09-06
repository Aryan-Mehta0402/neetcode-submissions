# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ans = []
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                curr = q.popleft()
                if curr:
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)
                    level.append(curr.val)
            if level:
                ans.append(level)

        return ans
