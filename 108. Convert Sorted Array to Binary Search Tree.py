# from typing import List, Optional


# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.recursive_bst(nums)

    def recursive_bst(self, nums: List[int]):

        if nums is None or len(nums)== 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.recursive_bst(nums[0:mid])
        root.right = self.recursive_bst(nums[mid+1: len(nums)])

        return root
