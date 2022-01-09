class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.post_order_traversal_helper(root, [])

    def post_order_traversal_helper(self, root, res):
        if root is None:
            return
        self.post_order_traversal_helper(root.left, res)
        self.post_order_traversal_helper(root.right, res)
        res.append(root.val)
        return res


root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(2)
root.right.right.right = TreeNode(2)

print("Post-order Traversal: ", Solution().postorderTraversal(root))