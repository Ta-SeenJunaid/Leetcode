# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.current_node = TreeNode(None)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        answer = self.current_node
        self.in_order_traversal(root)
        return answer.right

    def in_order_traversal(self, root: Optional[TreeNode]):
        if root:
            self.in_order_traversal(root.left)
            root.left = None
            self.current_node.right = root
            self.current_node = root
            self.in_order_traversal(root.right)

