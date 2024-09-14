# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.memo = {}
        def depth(root):
            if root in self.memo:
                return self.memo[root]
            if not root:
                return 0
            if not root.left:
                self.memo[root] = 1 + depth(root.right)
            if not root.right:
                self.memo[root] = 1 + depth(root.left)
            self.memo[root] = 1 + min(depth(root.left), depth(root.right))
            
            return self.memo[root]
        return depth(root)