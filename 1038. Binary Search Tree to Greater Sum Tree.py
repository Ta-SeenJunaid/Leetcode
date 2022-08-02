# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return root

    def dfs(self, node: TreeNode) -> TreeNode:
        if not node:
            return

        self.dfs(node.right)
        self.sum += node.val
        node.val = self.sum
        self.dfs(node.left)
        return





