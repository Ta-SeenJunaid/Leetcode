# https://leetcode.com/problems/convert-bst-to-greater-tree/solutions/1951325/python3-in-order-dfs-explained 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs_helper(root, 0)
        return root

    def dfs_helper(self, root, initial):
        if not root:
            return 0
        r_sum = self.dfs_helper(root.right, initial)
        prev, root.val = root.val, root.val + r_sum + initial
        l_sum = self.dfs_helper(root.left, root.val)
        return prev + l_sum + r_sum
        
