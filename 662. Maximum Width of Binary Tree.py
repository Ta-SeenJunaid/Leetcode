# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = []
        queue.append([root, 0])
        max_depth = 1
        while queue:
            _, min_idx = queue[0]
            for _ in range(len(queue)):
                node, cur_idx = queue.pop(0)
                idx = cur_idx - min_idx
                if node.left:
                    queue.append([node.left, 2 * idx + 1])
                if node.right:
                    queue.append([node.right, 2 * idx + 2])
            max_depth = max(max_depth, cur_idx - min_idx + 1) 
        return max_depth 
        
