# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.dfs_helper(root)
        return self.tilt

    def dfs_helper(self, root):
        if not root:
            return 0
        left = self.dfs_helper(root.left)
        right = self.dfs_helper(root.right)
        self.tilt += abs(left - right)
        return root.val + left + right
