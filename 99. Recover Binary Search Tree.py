# https://leetcode.com/problems/recover-binary-search-tree/editorial/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs_helper(root):
            nonlocal x, y, prev
            if not root:
                return
            dfs_helper(root.left)
            if prev and root.val < prev.val:
                y = root
                if x is None:
                    x = prev
                else:
                    return
            prev = root
            dfs_helper(root.right)
        x = y = prev = None
        dfs_helper(root)
        x.val, y.val = y.val, x.val
        
