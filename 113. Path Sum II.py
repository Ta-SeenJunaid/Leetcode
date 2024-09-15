# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs_helper(root, paths, target):
            if not root:
                return
            # elif target < 0:
            #     return
            paths.append(root.val)
            target = target - root.val
            if not target and not root.left and not root.right:
                ans.append(paths)
            dfs_helper(root.left, paths.copy(), target)
            dfs_helper(root.right, paths.copy(), target)
        dfs_helper(root, [], targetSum)
        return ans         
