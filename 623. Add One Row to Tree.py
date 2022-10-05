from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        self.dfs_helper(root, val, depth, 1)
        return root

    def dfs_helper(self, root: Optional[TreeNode], val: int, depth: int, current_depth: int):
        if root is None:
            return

        if depth == current_depth + 1:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
            return

        self.dfs_helper(root.left, val, depth, current_depth + 1)
        self.dfs_helper(root.right, val, depth, current_depth + 1)

