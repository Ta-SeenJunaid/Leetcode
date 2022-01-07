

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_leaf(root):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return True
    return False


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if root is not None:
            if is_leaf(root.left):
                sum += root.left.val
            else:
                sum += self.sumOfLeftLeaves(root.left)
            sum += self.sumOfLeftLeaves(root.right)

        return sum



