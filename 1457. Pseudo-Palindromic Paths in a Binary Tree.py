# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/discuss/2574552/Python3-DFS-TC-O(n)-SC-O(h)
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], counter: list[int]) -> int:
            counter[node.val - 1] = 0 if counter[node.val - 1] else 1
            if not (node.left or node.right):
                ret = 0 if sum(counter) > 1 else 1
            else:
                ret = 0
                if node.left:
                    ret = dfs(node.left, counter)
                if node.right:
                    ret += dfs(node.right, counter)
            counter[node.val - 1] = 0 if counter[node.val - 1] else 1
            return ret

        return dfs(root, [0] * 9)