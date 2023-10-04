# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue, result = [], []
        queue.append(root)
        while queue:
            cur_lev = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    cur_lev.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if cur_lev:
                result.append(cur_lev[-1])
        return result
      
