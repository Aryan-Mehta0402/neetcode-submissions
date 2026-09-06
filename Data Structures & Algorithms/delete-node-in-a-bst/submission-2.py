class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def dfs(node, parent):
            if not node:
                return None

            if node.val == key:
                return node, parent

            if node.val < key:
                return dfs(node.right, node)
            else:
                return dfs(node.left, node)

        def delete(node, parent):

            if parent is None:
                if not node.left and not node.right:
                    return None

                if not node.left:
                    return node.right

                if not node.right:
                    return node.left

                left_subtree = node.left
                right_subtree = node.right

                temp = left_subtree
                while temp.right:
                    temp = temp.right

                temp.right = right_subtree
                return left_subtree

            if node.left:
                left_subtree = node.left
                right_subtree = node.right

                if node == parent.left:
                    parent.left = left_subtree
                else:
                    parent.right = left_subtree

                temp = left_subtree
                while temp.right:
                    temp = temp.right

                temp.right = right_subtree

            else:
                if node == parent.left:
                    parent.left = node.right
                else:
                    parent.right = node.right

        result = dfs(root, None)

        if result is None:
            return root

        node, parent = result

        new_root = delete(node, parent)

        if parent is None:
            return new_root

        return root