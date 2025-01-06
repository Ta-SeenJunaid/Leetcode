# https://leetcode.com/problems/distribute-coins-in-binary-tree/editorial

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        def dfs(root):
            if not root:
                return 0
            nonlocal moves
            lc = dfs(root.left)
            rc = dfs(root.right)
            moves +=  abs(lc) + abs(rc)
            return root.val -1 + lc + rc
        dfs(root)
        return moves
        
