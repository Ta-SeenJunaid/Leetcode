# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# One key fact is not to take any negative path

class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs_helper(root)
        return self.max_sum

    def dfs_helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l_sum = max(0, self.dfs_helper(root.left))
        r_sum = max(0, self.dfs_helper(root.right))
        cur_sum = root.val + l_sum + r_sum
        self.max_sum = max(self.max_sum, root.val + l_sum + r_sum)
        return root.val + max(l_sum, r_sum)
