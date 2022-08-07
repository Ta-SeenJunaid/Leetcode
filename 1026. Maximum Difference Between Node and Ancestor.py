from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.dfs_helper(root)
        return self.ans

    def dfs_helper(self, root: Optional[TreeNode]):
        if not root:
            return root

        left_array = self.dfs_helper(root.left)
        right_array = self.dfs_helper(root.right)

        current_array = [root.val]
        if left_array:
            current_array = current_array + left_array
        if right_array:
            current_array = current_array + right_array
        for i in current_array[1:]:
            temp = abs(root.val-i)
            if temp > self.ans:
                self.ans = temp
        return current_array


root = TreeNode(8)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right = TreeNode(10)

solution = Solution()
print(solution.maxAncestorDiff(root))

