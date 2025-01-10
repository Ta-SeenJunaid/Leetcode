# https://leetcode.com/problems/largest-bst-subtree/solutions/4685590/python3-easy-explain-solution-beats-99
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def is_bst(root):
            if not root:
                return float("inf"), float("-inf"), True, 0
            nonlocal ans
            lmin, lmax, lt, ls = is_bst(root.left)
            rmin, rmax, rt, rs = is_bst(root.right)
            cbst = lt and rt and lmax < root.val < rmin 
            size = ls+rs+1
            if cbst:
                ans = max(ans, size)
            return min(lmin, rmin, root.val), max(lmax, rmax, root.val), cbst, size
        is_bst(root)
        return ans
