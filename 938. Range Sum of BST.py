# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum_ = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.in_order_traversal(root, low, high)
        return self.sum_

    def in_order_traversal(self, root: Optional[TreeNode], low: int, high: int):
        if root:
            if root.val > low:
                self.in_order_traversal(root.left, low, high)
            if low <= root.val <= high:
                self.sum_ += root.val
            if root.val < high:
                self.in_order_traversal(root.right, low, high)

