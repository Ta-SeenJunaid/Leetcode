# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/solutions/3314428/python-4-line-essence-pure-soul-based-preorder-dfs-solution

# The dictionary is initialized with one key-value pair: {None: None}. This allows the function to handle the case where the tree traversal encounters a None node. When None is encountered (as either left, right, or random), the copy of None is simply None.

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]', memo: 'dict[old:new]' = {None:None}) -> 'Optional[NodeCopy]':
        if root not in memo:
            memo[root] = NodeCopy(root.val)
            memo[root].left, memo[root].right, memo[root].random = self.copyRandomBinaryTree(root.left), self.copyRandomBinaryTree(root.right), self.copyRandomBinaryTree(root.random)
        return memo[root]
        
