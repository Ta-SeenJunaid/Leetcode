from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        return self.tree_traversal(root, result)

    def tree_traversal(self, root: 'Node', result: List[int]):
        if not root:
            return
        for i in root.children:
            self.tree_traversal(i, result)
        result.append(root.val)
        return result

