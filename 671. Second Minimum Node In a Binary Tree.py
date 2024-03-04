# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.mini = 2**32
        self.root = None

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.root = root
        self.dfs_helper(root)
        return -1 if self.mini == 2**32 else self.mini

    def dfs_helper(self, root):
        if not root:
            return
        if root.val != self.root.val:
            self.mini = min(self.mini, root.val)
        self.dfs_helper(root.left)
        self.dfs_helper(root.right)

        
