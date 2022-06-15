# https://www.youtube.com/watch?v=30WqiTVp8Kc
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        stack = []
        for val in preorder:
            node = TreeNode(val)
            if not root:
                root = node
            elif val < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and stack[-1].val < val:
                    pop_node = stack.pop()
                pop_node.right = node
            stack.append(node)
        return root
