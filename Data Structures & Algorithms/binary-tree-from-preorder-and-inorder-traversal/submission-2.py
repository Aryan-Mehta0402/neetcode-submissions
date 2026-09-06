class Solution:
    def buildTree(self, p: List[int], i: List[int]) -> Optional[TreeNode]:

        # value -> index in inorder
        pos = {val: idx for idx, val in enumerate(i)}

        def dfs(preL, preR, inL, inR):
            if preL > preR or inL > inR:
                return None

            # First element of preorder is the root
            root_val = p[preL]
            root = TreeNode(root_val)

            # Position of root in inorder
            mid = pos[root_val]

            # Number of nodes in left subtree
            left_size = mid - inL

            # Left subtree
            root.left = dfs(
                preL + 1,
                preL + left_size,
                inL,
                mid - 1
            )

            # Right subtree
            root.right = dfs(
                preL + left_size + 1,
                preR,
                mid + 1,
                inR
            )

            return root

        return dfs(0, len(p) - 1, 0, len(i) - 1)