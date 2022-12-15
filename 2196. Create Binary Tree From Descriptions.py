from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tracker = {}
        is_child = set()
        for p, c, is_left in descriptions:
            if p not in tracker:
                tracker[p] = TreeNode(p, None, None)
            if c not in tracker:
                tracker[c] = TreeNode(c, None, None)
            if is_left:
                tracker[p].left = tracker[c]
            else:
                tracker[p].right = tracker[c]
            is_child.add(c)
        for i, _, _ in descriptions:
            if i not in is_child:
                return tracker[i]





