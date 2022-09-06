from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs_helper(root)

    def dfs_helper(self, root: Optional[TreeNode]):
        if not root:
            return None
        self.dfs_helper(root.left)
        self.dfs_helper(root.right)

        if root.left:
            if root.left.val == 0 and root.left.left is None and root.left.right is None:
                root.left = None
        if root.right:
            if root.right.val == 0 and root.right.left is None and root.right.right is None:
                root.right = None
        if root.val == 0 and root.left is None and root.right is None:
            root = None

        return root
