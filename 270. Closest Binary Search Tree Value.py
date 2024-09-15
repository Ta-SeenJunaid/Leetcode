# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_ = float('inf') 
        ans = 0
        def dfs_helper(root):
            nonlocal ans
            nonlocal min_
            if not root:
                return
            if abs(target - root.val) < min_:
                min_ = abs(target - root.val)
                ans = root.val
            elif  abs(target - root.val) == min_ :
                ans = min(ans, root.val)
            dfs_helper(root.left)
            dfs_helper(root.right)
        dfs_helper(root)
        return ans
