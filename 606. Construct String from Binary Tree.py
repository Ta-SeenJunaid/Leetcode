from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.current_string = []

    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.dfs_helper(root)
        return ''.join(self.current_string)[1:-1]

    def dfs_helper(self, root: Optional[TreeNode]):
        if root is None:
            return None

        self.current_string.append("(")
        self.current_string.append(str(root.val))
        self.dfs_helper(root.left)
        if root.right and not root.left:
            self.current_string.append("()")
            self.dfs_helper(root.right)
        else:
            self.dfs_helper(root.right)
        self.current_string.append(")")
