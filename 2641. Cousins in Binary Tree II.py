# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l_sum = []
        q = [root]
        while q:
            t_sum = 0
            for _ in range(len(q)):
                node = q.pop(0)
                if node:
                    t_sum += node.val
                    q.append(node.left)
                    q.append(node.right)
            l_sum.append(t_sum)
        def dfs(root, level, sib_val):
            if not root:
                return
            root.val = l_sum[level] - sib_val - root.val
            lcv = root.left.val if root.left else 0
            rcv = root.right.val if root.right else 0
            dfs(root.left, level+1, rcv)
            dfs(root.right, level+1, lcv)
        dfs(root, 0, 0) 
        return root
        
