# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.dfs_helper(root, root.val)
        
    def dfs_helper(self, root, val):
        if not root:
            return True
        if root.val != val:
            return False
        return self.dfs_helper(root.left, val) and self.dfs_helper(root.right, val)
