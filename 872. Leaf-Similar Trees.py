# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.leaf1 = []
        self.leaf2 = []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.dfs_helper(root1, 1)
        self.dfs_helper(root2, 2)
        return self.leaf1==self.leaf2

    def dfs_helper(self, root, tree):
        if not root:
            return
        if not root.left and not root.right:
            if tree==1:
                self.leaf1.append(root.val)
            else:
                self.leaf2.append(root.val)
            return
        self.dfs_helper(root.left, tree)
        self.dfs_helper(root.right, tree)
