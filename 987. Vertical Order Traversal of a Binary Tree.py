# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        dictionary = defaultdict(list)
        queue.append([root, 0, 0])
        while queue:
            for idx in range(len(queue)):
                node, row, col = queue.pop(0)
                if node:
                    dictionary[col].append((row, node.val))
                    if node.left:
                        queue.append([node.left, row + 1, col - 1])
                    if node.right:
                        queue.append([node.right, row + 1, col + 1])
        result = []
        for col in sorted(dictionary.keys()):
            col_val = [val for _, val in sorted(dictionary[col])]
            result.append(col_val)
        return result
      
