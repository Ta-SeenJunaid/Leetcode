# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return False if self.dfs_helper(root) == -1 else True
     
    def dfs_helper(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        ld = self.dfs_helper(root.left)
        rd = self.dfs_helper(root.right)
        if ld == -1 or rd == -1:
            return -1
        if abs(ld-rd) > 1:
            return -1
        return 1 + max(ld, rd)
