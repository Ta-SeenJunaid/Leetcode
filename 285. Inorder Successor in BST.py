# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        min_ = float('inf')
        def dfs_helper(root, p):
            if not root:
                return None
            nonlocal min_
            left = dfs_helper(root.left, p)
            if root.val > p.val:
                if min_ > root.val-p.val:
                    min_ = min(min_, root.val-p.val)
                    return root
            right = dfs_helper(root.right, p)
            return left or right 
        return dfs_helper(root, p)
        
