# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def dfs_helper(root):
            nonlocal ans
            if not root:
                return 0
            cur_level = max(dfs_helper(root.left), dfs_helper(root.right))
            if cur_level >= len(ans):
                ans.append([])
            ans[cur_level].append(root.val)
            return cur_level + 1
        _ = dfs_helper(root)
        return ans
        
