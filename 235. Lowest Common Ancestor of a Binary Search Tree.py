# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs_helper(root, p, q, 0)
        return self.ans

    def dfs_helper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', count):
        if not root:
            return 0

        left_count = self.dfs_helper(root.left, p, q, count)
        right_count = self.dfs_helper(root.right, p, q, count)

        if root.val == p.val or root.val == q.val:
            count += 1

        if count + left_count + right_count == 2 and self.ans is None:
            self.ans = root

        print(root.val, count, left_count, right_count)

        return count + left_count + right_count
