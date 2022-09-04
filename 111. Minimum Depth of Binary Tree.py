# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return result
        queue = [root]
        while queue:
            queue_len = len(queue)
            result += 1
            for i in range(queue_len):
                node = queue.pop(0)
                if node:
                    if not node.left and not node.right:
                        return result
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return result