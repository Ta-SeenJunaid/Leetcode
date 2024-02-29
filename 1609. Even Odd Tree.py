# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        even = True
        while queue:
            start = True
            prev = float('inf')
            if even:
                prev = float('-inf')
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    if even and (node.val%2 == 0 or node.val <= prev):
                        return False
                    if not even and (node.val%2 != 0 or node.val >= prev):
                        return False
                    prev = node.val
                    queue.append(node.left)
                    queue.append(node.right)
            even = not even 
        return True        
