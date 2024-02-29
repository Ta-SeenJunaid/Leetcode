# In order traversal will give the shorted sequence in BST 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0
        self.ans = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs_helper(root, k)
        return self.ans

    def dfs_helper(self, root, k):
        if not root:
            return
        self.dfs_helper(root.left, k)
        self.count +=1
        if self.count == k:
            self.ans = root.val
            return
        self.dfs_helper(root.right, k)
        
