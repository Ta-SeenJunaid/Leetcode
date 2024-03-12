# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/editorial/?envType=daily-question&envId=2024-03-12 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(val=0, next=head)
        start=front
        while start != None:
            prefix_sum = 0
            end = start.next
            while end != None:
                prefix_sum += end.val
                if prefix_sum == 0:
                    start.next = end.next
                end = end.next
            start = start.next
        return front.next
            
        
