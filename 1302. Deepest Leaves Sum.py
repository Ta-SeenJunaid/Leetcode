# https://dev.to/seanpgallivan/solution-deepest-leaves-sum-1936
# https://www.youtube.com/watch?v=fpdF1CeU70U
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        sum_ = []

        def dfs(node: TreeNode, lvl: int):
            if len(sum_) == lvl:
                sum_.append(node.val)
            else:
                sum_[lvl] += node.val
            if node.left:
                dfs(node.left, lvl+1)
            if node.right:
                dfs(node.right, lvl+1)
        dfs(root, 0)
        return sum_[-1]
