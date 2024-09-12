# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.temp = defaultdict(list)

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        test = self.dfs_helper(root)
        print(self.temp)
        return list(self.temp.values())

    def dfs_helper(self, root):
        if not root:
            return 0
        left = self.dfs_helper(root.left)
        right = self.dfs_helper(root.right)
        self.temp[max(left, right)].append(root.val)
        return 1+max(left, right)
        
