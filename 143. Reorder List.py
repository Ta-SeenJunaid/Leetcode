# https://leetcode.com/problems/reorder-list/solutions/4912462/super-easy-fast-slow-pointer-c-java-python-solution-with-detailed-explanation

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Step 1: find the middle of the list
        first, slow = head, head
        while first and first.next:
            first = first.next.next
            slow = slow.next

        # Step 2: reverse the 2nd half
        rev_list = None
        while slow:
            temp = slow.next
            slow.next = rev_list
            rev_list = slow
            slow = temp

        # Step 3: merge the 2 list
        forwd_list = head
        while rev_list.next:
            temp_f = forwd_list.next
            temp_r = rev_list.next

            forwd_list.next = rev_list
            rev_list.next = temp_f

            forwd_list = temp_f
            rev_list = temp_r


        
