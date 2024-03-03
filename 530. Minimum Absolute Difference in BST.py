# with Inorder we can compare biggest value in left tree, root and smallest value in right tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.min_dif = float('inf')
        self.last_value = None

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.dfs_inorder(root)
        return self.min_dif
    
    def dfs_inorder(self, root):
        if not root:
            return 
        self.dfs_inorder(root.left)
        if self.last_value != None:
            self.min_dif = min(self.min_dif, abs(root.val-self.last_value))
        self.last_value = root.val
        right = self.dfs_inorder(root.right)

