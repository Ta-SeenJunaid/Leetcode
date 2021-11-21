# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = {}

        self.traverse(root, counter)
        max_value = max(counter.values())

        mode = []
        for key, value in counter.items():
            if value == max_value:
                mode.append(key)

        return mode


    def traverse(self, root, counter):
        if not root:
            return None

        counter[root.val] = counter.get(root.val, 0) + 1

        self.traverse(root.left, counter)
        self.traverse(root.right, counter)
