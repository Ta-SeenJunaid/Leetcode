from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.sorted_list = []
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.dfs_inorder_traversal(root)
        return self.bfs_construct(0,len(self.sorted_list)-1)

    def dfs_inorder_traversal(self, root: Optional[TreeNode]):
        if root is None:
            return root
        self.dfs_inorder_traversal(root.left)
        self.sorted_list.append(root.val)
        self.dfs_inorder_traversal(root.right)

    def bfs_construct(self, left, right):
        if left==right:
            return TreeNode(self.sorted_list[left])
        if left > right:
            return None
        mid = (left+right)//2
        root = TreeNode()
        root.val = self.sorted_list[mid]
        root.left = self.bfs_construct(left, mid-1)
        root.right = self.bfs_construct(mid+1, right)
        return root
