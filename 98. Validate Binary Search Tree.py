# https://www.youtube.com/watch?v=s6ATEkipzow
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs_helper(root, float('-inf'), float('inf'))

    def dfs_helper(self, root: Optional[TreeNode], low, high):
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False

        return self.dfs_helper(root.left, low, root.val) and self.dfs_helper(
            root.right, root.val, high)


