# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_d = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        temp = self.dfs_helper(root)
        return self.max_d

    def dfs_helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ld = self.dfs_helper(root.left)
        rd = self.dfs_helper(root.right)
        self.max_d = max(self.max_d, ld + rd)
        return 1 + max(ld, rd)
