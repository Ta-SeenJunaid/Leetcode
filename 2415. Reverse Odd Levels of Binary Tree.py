from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        odd_level = False
        queue = [root]
        while queue:
            queue_len = len(queue)
            memory = []
            node_memory = []
            for i in range(queue_len):
                node = queue.pop(0)
                if node:
                    if odd_level:
                        memory.append(node.val)
                        node_memory.append(node)
                    queue.append(node.left)
                    queue.append(node.right)
            if odd_level:
                for node in node_memory:
                    node.val = memory.pop()
            odd_level = not odd_level
        return root

