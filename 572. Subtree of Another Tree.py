# https://leetcode.com/problems/subtree-of-another-tree/solutions/4273768/depth-first-search-o-n-2-python-step-by-step-explanation

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if self.same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same(self, root, sub_root):
        if not root and not sub_root:
            return True
        if root and sub_root and root.val == sub_root.val:
            return self.same(root.left, sub_root.left) and self.same(root.right, sub_root.right)
        return False
