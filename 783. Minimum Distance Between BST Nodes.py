from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sorted_list = []

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # If you use in-order traversal to traverse the tree,
        # it will always give you a sorted list
        self.dfs_helper(root)
        result = float('inf')
        for i in range(1, len(self.sorted_list)):
            result = min(result, self.sorted_list[i]-self.sorted_list[i-1])
        return result

    def dfs_helper(self, root: Optional[TreeNode]):
        if not root:
            return None
        self.dfs_helper(root.left)
        self.sorted_list.append(root.val)
        self.dfs_helper(root.right)
