# https://www.youtube.com/watch?v=doj95MelfSA

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow 
            slow = temp
        max_tsum = 0
        while slow:
            max_tsum = max(max_tsum, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        return  max_tsum
        
