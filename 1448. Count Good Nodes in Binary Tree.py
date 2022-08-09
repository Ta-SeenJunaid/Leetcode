# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs_helper(root: TreeNode, max_value):
            if not root:
                return 0
            max_value = max(root.val, max_value)
            if root.val == max_value:
                self.result += 1
            dfs_helper(root.left, max_value)
            dfs_helper(root.right, max_value)

        dfs_helper(root, root.val)
        return self.result


root = TreeNode(8)
root.right = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(8)
root.right.right.right = TreeNode(4)


solution = Solution()
print(solution.goodNodes(root))
