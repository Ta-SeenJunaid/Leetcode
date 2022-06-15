# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.combined_list = []

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.in_order_traversal(root1)
        self.in_order_traversal(root2)
        self.combined_list.sort()
        return self.combined_list

    def in_order_traversal(self, root: TreeNode):
        if root:
            self.in_order_traversal(root.left)
            self.combined_list.append(root.val)
            self.in_order_traversal(root.right)