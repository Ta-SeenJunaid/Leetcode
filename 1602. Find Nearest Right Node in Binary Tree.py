# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        q = [root]
        while q:
            q_len = len(q)
            found = False
            for i in range(q_len):
                n = q.pop(0)
                if found:
                    return n
                if n.val==u.val:
                    found = True
                    if i==q_len-1:
                        return None
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return None
