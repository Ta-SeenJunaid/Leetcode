"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_path = defaultdict()
        def path(root):
            if not root:
                return
            p_path[root.val] = root
            path(root.parent)
        path(p)
        def lca(root):
            if root.val in p_path:
                return p_path[root.val]
            return lca(root.parent)
        return lca(q)
        
