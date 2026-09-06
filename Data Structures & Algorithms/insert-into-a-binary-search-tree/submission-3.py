# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)
        
        def insert(node):
            if node.val < val and node.right is None:
                node.right = TreeNode(val)
            elif node.val < val:
                insert(node.right)
            elif node.val > val and node.left is None:
                node.left = TreeNode(val)
            else:
                insert(node.left)

        insert(root)
    
        return root
