from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.temp = []

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.dfs_helper(root, k)

    def dfs_helper(self, root: Optional[TreeNode], k: int):
        if not root:
            return False
        # x + y = k, y = k - x
        y = k - root.val
        if y in self.temp:
            return True
        self.temp.append(root.val)
        return self.dfs_helper(root.left, k) or self.dfs_helper(root.right, k)
