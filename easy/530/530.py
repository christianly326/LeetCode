# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.difference = float('inf')
        self.prev = None
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            print(root.val, self.prev.val if self.prev else 'None')
            if self.prev:
                self.difference = min(abs(root.val - self.prev.val), self.difference)
            self.prev = root
            inorder(root.right)
            return
        inorder(root)
        return self.difference
