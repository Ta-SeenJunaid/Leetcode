from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        queue = []
        if not root:
            return root

        queue.append(root)
        while queue:
            queue_len = len(queue)
            level = []
            for i in range(queue_len):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    if node.children:
                        for j in node.children:
                            queue.append(j)
            if level:
                result.append(level)

        return result


