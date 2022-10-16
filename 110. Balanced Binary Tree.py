from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        elif self.dfs_helper(root):
            return True
        else:
            return False

    def dfs_helper(self, root: Optional[TreeNode]):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left_r = self.dfs_helper(root.left)
        right_r = self.dfs_helper(root.right)
        if left_r is False or right_r is False:
            return False
        if abs(left_r - right_r) > 1:
            return False
        return max(left_r, right_r) + 1

