# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        dict_o = defaultdict(list)
        q = [(root, 0)]
        min_r, max_r = 0,0
        while q:
            node, index = q.pop(0)
            dict_o[index].append(node.val)
            min_r = min(min_r, index)
            max_r = max(max_r, index)
            if node.left:
                q.append((node.left, index-1))
            if node.right:
                q.append((node.right, index+1))
        return [dict_o[i] for i in range(min_r, max_r+1)]

        
