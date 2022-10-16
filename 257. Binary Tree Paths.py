from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.paths = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.dfs_helper(root, [])
        for i in range(len(self.paths)):
            self.paths[i] = "".join(self.paths[i])
        return self.paths

    def dfs_helper(self, root: Optional[TreeNode], current_path):
        if not root:
            return None
        current_path.append(str(root.val))
        if not root.left and not root.right:
            self.paths.append(current_path)
            return
        current_path.append("->")
        current_path_copy = current_path.copy()
        self.dfs_helper(root.left, current_path)
        self.dfs_helper(root.right, current_path_copy)


