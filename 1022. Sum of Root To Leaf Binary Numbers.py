from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.dfs_helper(root, str(root.val))
        return self.ans

    def dfs_helper(self, node: Optional[TreeNode], current_string):
        if not node.left and not node.right:
            self.ans += int(current_string, 2)
            return

        if node.left:
            self.dfs_helper(node.left, current_string+str(node.left.val))
        if node.right:
            self.dfs_helper(node.right, current_string+str(node.right.val))


