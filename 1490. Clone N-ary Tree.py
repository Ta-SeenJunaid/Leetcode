"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        copy_n = Node(val=root.val)
        for c in root.children:
            copy_n.children.append(self.cloneTree(c))
        return copy_n
        
