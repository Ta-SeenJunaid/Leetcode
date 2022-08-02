# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.dfs(root)
        return self.ans

    def dfs(self, node: Optional[TreeNode]):
        if not node:
            return 0, 0

        left_sum, left_count = self.dfs(node.left)
        right_sum, right_count = self.dfs(node.right)

        if (node.val + left_sum + right_sum)//(1 + left_count + right_count) == node.val:
            self.ans += 1

        return node.val + left_sum + right_sum, 1 + left_count + right_count





