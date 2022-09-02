# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result  = []
        import collections
        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)
            level = []
            for i in range(queue_len):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if level:
                import statistics
                result.append(statistics.mean(level))
        return result


