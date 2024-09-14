class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = [0]
        def traverse(root):
            if not root:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            self.diameter[0] = max(self.diameter[0], left + right)
            return 1 + max(left, right)
        traverse(root)
        return self.diameter[0]