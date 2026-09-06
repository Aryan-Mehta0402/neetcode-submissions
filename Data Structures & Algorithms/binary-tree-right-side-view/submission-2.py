# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            for i in range(qlen-1):
                curr = q.popleft()
                if curr:
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)
            cur = q.popleft()
            if cur:
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                ans.append(cur.val)

        return ans