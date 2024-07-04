# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modify = head.next
        next_sum = modify
        while next_sum:
            sum = 0
            while next_sum.val != 0:
                sum += next_sum.val
                next_sum = next_sum.next
            modify.val = sum
            next_sum = next_sum.next
            modify.next = next_sum
            modify = modify.next
        return head.next
        
