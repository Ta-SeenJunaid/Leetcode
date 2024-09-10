# https://leetcode.com/problems/binary-tree-upside-down/solutions/1214661/python-3-simple-concise-dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs_helper(node, parent):
            if not node:
                return parent
            res = dfs_helper(node.left, node)
            node.right = parent
            if parent:
                node.left = parent.right
            else:
                node.left = None
            return res
        return dfs_helper(root, None)

        
