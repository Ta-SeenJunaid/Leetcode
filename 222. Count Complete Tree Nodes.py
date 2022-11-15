from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.dfs_helper(root)
        return self.count

    def dfs_helper(self, root: Optional[TreeNode]):
        if not root:
            return
        self.count +=1
        self.dfs_helper(root.left)
        self.dfs_helper(root.right)

