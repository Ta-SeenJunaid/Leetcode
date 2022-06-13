# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.node_finder(original, cloned, target)

    def node_finder(self, original: TreeNode, cloned: TreeNode, target: TreeNode):
        if not original:
            return None
        if original==target:
            return cloned
        return self.node_finder(original.left, cloned.left, target) or \
               self.node_finder(original.right, cloned.right, target)
