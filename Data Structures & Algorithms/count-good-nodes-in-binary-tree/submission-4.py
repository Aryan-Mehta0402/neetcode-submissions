# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root is good by default
        # use bfs and store prev max on that path
        # if node.val >= max then good node and max update

        cnt = 0
        q = deque()
        q.append([root, root.val]) # [node, max on that path including the node]

        while q:
            curr, maxx = q.popleft()
            if curr:
                left = curr.left
                right = curr.right

                if curr.val >= maxx:
                    cnt += 1

                if left:
                    q.append([left, max(left.val, maxx)]) 
                if right:
                    q.append([right, max(right.val, maxx)])

        return cnt

