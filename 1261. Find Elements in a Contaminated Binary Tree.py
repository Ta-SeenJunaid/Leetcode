from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.memory = set()
        if self.root:
            self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.memory

    def dfs(self, root:Optional[TreeNode], val):
        if not root:
            return
        root.val = val
        self.memory.add(val)
        self.dfs(root.left, 2*val+1)
        self.dfs(root.right, 2*val+2)
