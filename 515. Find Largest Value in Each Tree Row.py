# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        q = [root]
        while q:
            cur_max = float("-inf")
            for _ in range(len(q)):
                node = q.pop(0)
                cur_max = max(cur_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(cur_max)
        return ans    
