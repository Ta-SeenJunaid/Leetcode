# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        ans = root.val
        while queue:
            left = True
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    if left:
                        ans = node.val
                    left = False
                    queue.append(node.left)
                    queue.append(node.right)
        return ans
