from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total_sum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs_helper(root, '0')
        return self.total_sum

    def dfs_helper(self, root: Optional[TreeNode], current_string):
        if not root:
            return None
        current_string = current_string + str(root.val)
        if not root.left and not root.right:
            self.total_sum += int(current_string)
            return
        self.dfs_helper(root.left, current_string)
        self.dfs_helper(root.right, current_string)
        return
