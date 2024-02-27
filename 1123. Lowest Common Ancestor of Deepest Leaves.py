# If the node in question has maximum depth, it is the answer.

# If both the left and right child of a node have a deepest descendant, then the answer is this parent node.

# Otherwise, if some child has a deepest descendant, then the answer is that child.

# Otherwise, the answer for this subtree doesn't exis

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.ans = None
        self.max_dep = 0
 
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs_helper(root, 0)
        return self.ans

    def dfs_helper(self, root, depth):
        if not root:
            return 0
        left_d = self.dfs_helper(root.left, depth + 1)
        right_d = self.dfs_helper(root.right, depth + 1)
        self.max_dep = max(self.max_dep, depth)
        if depth == self.max_dep:
            self.ans = root
        if left_d == right_d == self.max_dep:
            self.ans = root
        return max(left_d, right_d, depth)       
        
