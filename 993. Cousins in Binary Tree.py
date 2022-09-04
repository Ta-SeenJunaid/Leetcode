# https://www.youtube.com/watch?v=PyfLrJvoC_s
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.x_info = []
        self.y_info = []

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.dfs_helper(root, x, y, 0, None)
        return self.x_info[0][0] == self.y_info[0][0] and \
               self.x_info[0][1] != self.y_info[0][1]

    def dfs_helper(self, root, x, y, depth, parent):
        if root is None:
            return None

        if root.val == x:
            self.x_info.append((depth, parent))
        if root.val == y:
            self.y_info.append((depth, parent))
        if self.x_info and self.y_info:
            return

        self.dfs_helper(root.left, x, y, depth + 1, root)
        self.dfs_helper(root.right, x, y, depth + 1, root)
