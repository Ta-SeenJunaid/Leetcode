# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.dfs_helper(root, [])

    def dfs_helper(self, root: Optional[TreeNode], res) -> List[int]:
        if not root:
            return
        res.append(root.val)
        self.dfs_helper(root.left, res)
        self.dfs_helper(root.right, res)
        return res


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack, ans = [], []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans

