# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.forest = []

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        root = self.dfs_helper(root, to_delete)
        if root:
            self.forest.append(root)
        return self.forest

    def dfs_helper(self, root, to_delete):
        if not root:
            return None
        root.left = self.dfs_helper(root.left, to_delete)
        root.right = self.dfs_helper(root.right, to_delete)
        if root.val in to_delete:
            if root.left is None and root.right is None:
                return None
            else:
                if root.left:
                    self.forest.append(root.left)
                if root.right:
                    self.forest.append(root.right)
            return None
        return root

        
