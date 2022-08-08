# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.dfs_helper(root)
        return self.sum

    def dfs_helper(self, root: TreeNode):
        if not root:
            return root

        if root.val % 2 == 0:
            if root.left:
                if root.left.left:
                    self.sum += root.left.left.val
                if root.left.right:
                    self.sum += root.left.right.val
            if root.right:
                if root.right.left:
                    self.sum += root.right.left.val
                if root.right.right:
                    self.sum += root.right.right.val
        self.dfs_helper(root.left)
        self.dfs_helper(root.right)

